import 'styles/global.scss';
import Vue from 'vue';
import { mapState, mapMutations, mapActions } from 'vuex';
import VModal from 'vue-js-modal';
import Notifications from 'vue-notification';
// import VTooltip from 'v-tooltip';
import Treeselect from '@riophae/vue-treeselect';
import VeeValidate, { Validator } from 'vee-validate';
import es from 'vee-validate/dist/locale/es';
import Search from 'components/Search';
import Patient from 'components/Patient';
import Addresses from 'components/Addresses';
import Units from 'components/Units';
// import Timers from 'components/Timers';
import Derivation from 'components/Derivation';
import map from 'lodash/fp/map';
import store from 'store';
import {
  MODAL_CHANGE_TAB,
  MODAL_RESET,
  EMERGENCY_TOGGLE_ACTIVE,
} from 'store/constants';

// Instantiate Vue mixins
// Vue.use(VTooltip);
Vue.use(Notifications);
Vue.use(VModal);
Vue.use(Treeselect);
Vue.use(VeeValidate, { inject: false });
Validator.localize('es', es);

// Initialize the Vue instance and assign to aforementioned global object
window.Erste.modal = new Vue({
  el: '#v-header',
  delimiters: ['<%', '%>'],
  components: { Search, Patient, Addresses, Units, Derivation },
  data() {
    return {
      tabs: [
        { name: 'search', label: 'Buscar' },
        { name: 'patient', label: 'Paciente' },
        { name: 'address', label: 'Dirección' },
        { name: 'units', label: 'Unidad' },
        { name: 'derivation', label: 'Derivacion' },
        // { name: 'timers', label: 'Timers' },
        // temporarily lock
        // { name: 'timers', label: 'Timers' },
      ],
    };
  },
  computed: {
    form() {
      const emergency = {
        ...this.emergency,
        final_address: this.address,
        units: map(unit => unit.id)(this.selected),
      };

      return emergency;
    },
    ...mapState(['loading', 'emergency', 'selected']),
    ...mapState({
      active: state => state.modal.active,
      search: state => state.modal.search,
      address: state => state.modal.address,
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
      this.$validator
        .validateAll('emergency')
        .then(valid => {
          if (valid) {
            return this.newIncident(this.form);
          }
          throw new Error();
        })
        .then(() => {
          this.$notify({
            text: 'Se ha guardado el auxilio en el sistema.',
            type: 'success',
          });
          // close modal after submit if no errors
          this.$modal.hide('incident-modal');
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
