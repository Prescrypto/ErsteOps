import 'styles/global.scss';
import Vue from 'vue';
import { mapState, mapMutations, mapActions } from 'vuex';
import VModal from 'vue-js-modal';
import VeeValidate from 'vee-validate';
import Search from 'components/Search';
import Patient from 'components/Patient';
import Addresses from 'components/Addresses';
import store from 'store';
import { MODAL_CHANGE_TAB, MODAL_RESET } from 'store/constants';

// Instantiate Vue mixins
Vue.use(VModal);
Vue.use(VeeValidate);

// Initialize the Vue instance and assign to aforementioned global object
window.Erste.modal = new Vue({
  el: '#v-header',
  delimiters: ['<%', '%>'],
  components: { Search, Patient, Addresses },
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
    ...mapState(['loading', 'emergency']),
    ...mapState({
      active: state => state.modal.active,
      search: state => state.modal.search,
    }),
  },
  store,
  methods: {
    ...mapMutations({
      changeTab: MODAL_CHANGE_TAB,
      reset: MODAL_RESET,
    }),
    tab() {
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
    submit(e) {
      e.preventDefault();
      this.newIncident(this.emergency);
    },
    ...mapActions(['newIncident']),
  },
});
