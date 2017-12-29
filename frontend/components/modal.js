import Vue from 'vue';
import VModal from 'vue-js-modal';

// Instantiate Vue Modal mixin
Vue.use(VModal);

// Initialize the Vue instance and assign to aforementioned global object
window.Erste.modal = new Vue({
  el: '#v-modal',
  methods: {
    show() {
      this.$modal.show('incident-modal');
    },
    hide() {
      this.$modal.hide('incident-modal');
    },
  },
});
