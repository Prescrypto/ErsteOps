import Vue from 'vue';

// Initialize the Vue instance and assign to aforementioned global object
window.Erste.nav = new Vue({
  el: '#v-nav',
  methods: {
    showModal() {
      window.Erste.modal.show();
    },
  },
});
