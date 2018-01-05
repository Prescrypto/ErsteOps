import Vue from 'vue';
import VModal from 'vue-js-modal';
import VeeValidate from 'vee-validate';
import Search from 'components/Search';
import store from 'store';

// Instantiate Vue mixins
Vue.use(VModal);
Vue.use(VeeValidate);

// Initialize the Vue instance and assign to aforementioned global object
window.Erste.modal = new Vue({
  el: '#v-header',
  delimiters: ['<%', '%>'],
  components: { Search },
  data() {
    return {
      search: true,
      tabs: [
        { name: 'search', label: 'Buscar' },
        { name: 'patient', label: 'Paciente' },
        { name: 'address', label: 'Dirección' },
        { name: 'units', label: 'Unidad' },
        { name: 'timers', label: 'Timers' },
      ],
      active: 'search',
    };
  },
  store,
  methods: {
    show() {
      this.$modal.show('incident-modal');
    },
    hide() {
      this.$modal.hide('incident-modal');
    },
    toggle(e) {
      const { name } = e.currentTarget.dataset;
      this.active = name;
    },
  },
});
