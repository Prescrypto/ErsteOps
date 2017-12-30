import Vue from 'vue';
import DashboardLog from 'components/DashboardLog';

// Initialize Vue component from HTML
const root = new Vue({
  el: '#dashboard-log',
  render: h => h(DashboardLog),
});

export default root;
