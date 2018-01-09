import Vue from 'vue';
import DashboardLog from 'components/DashboardLog';
import store from 'store';

// Initialize Vue component from HTML
const root = new Vue({
  el: '#dashboard-log',
  render: h => h(DashboardLog),
  store,
});

export default root;
