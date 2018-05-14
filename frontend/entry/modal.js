import 'styles/global.scss';
import Vue from 'vue';
import { mapState, mapMutations, mapActions } from 'vuex';
import VModal from 'vue-js-modal';
import Notifications from 'vue-notification';
import VeeValidate, { Validator } from 'vee-validate';
import es from 'vee-validate/dist/locale/es';
import Search from 'components/Search';
import Patient from 'components/Patient';
import Addresses from 'components/Addresses';
import Units from 'components/Units';
import map from 'lodash/fp/map';
import store from 'store';
import {
  MODAL_CHANGE_TAB,
  MODAL_RESET,
  EMERGENCY_TOGGLE_ACTIVE,
} from 'store/constants';

// Instantiate Vue mixins
Vue.use(Notifications);
Vue.use(VModal);
Vue.use(VeeValidate, { inject: false });
Validator.localize('es', es);

// Initialize the Vue instance and assign to aforementioned global object
window.Erste.modal = new Vue({
  el: '#v-header',
  delimiters: ['<%', '%>'],
  components: { Search, Patient, Addresses, Units },
  data() {
    return {
      tabs: [
        { name: 'search', label: 'Buscar' },
        { name: 'patient', label: 'Paciente' },
        { name: 'address', label: 'Dirección' },
        { name: 'units', label: 'Unidad' },
        // temporarily lock
        // { name: 'timers', label: 'Timers' },
      ],
    };
  },
  computed: {
    ...mapState(['loading', 'emergency', 'selected']),
    ...mapState({
      active: state => state.modal.active,
      search: state => state.modal.search,
    }),
  },
  store,
  methods: {
    ...mapMutations({
      toggleEmergency: EMERGENCY_TOGGLE_ACTIVE,
      changeTab: MODAL_CHANGE_TAB,
      reset: MODAL_RESET,
    }),
    open() {
      window.$(`#nav-${this.active}-tab`).tab('show');
    },
    destroy() {
      this.reset();
    },
    show() {
      this.$modal.show('incident-modal');
    },
    hide() {
      this.$modal.hide('incident-modal');
    },
    toggle(e) {
      const { name } = e.currentTarget.dataset;
      this.changeTab(name);
    },
    toggleActive(e) {
      e.preventDefault();
      this.toggleEmergency();
    },
    submit(e) {
      e.preventDefault();
      const emergency = {
        ...this.emergency,
        units: map(unit => unit.id)(this.selected),
      };
      this.$validator
        .validateAll('emergency')
        .then(valid => {
          if (valid) {
            return this.newIncident(emergency);
          }
          throw new Error();
        })
        .then(() => {
          this.$notify({
            text: 'Se ha guardado el auxilio en el sistema.',
            type: 'success',
          });
        })
        .catch(() => {
          this.$notify({
            text: 'Hubo un error al guardar el auxilio, intente de nuevo.',
            type: 'error',
          });
        });
    },
    ...mapActions(['newIncident']),
  },
  $_veeValidate: {
    validator: 'new',
  },
});
