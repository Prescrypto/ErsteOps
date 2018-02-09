import Vue from 'vue';
import DashboardLog from 'components/DashboardLog';
import Analytics from 'components/Analytics';
import store from 'store';

// Initialize Vue component from HTML
const dashboard = new Vue({
  el: '#dashboard-log',
  render: h => h(DashboardLog),
  store,
});

const analytics = new Vue({
  el: '#analytics',
  render: h => h(Analytics),
  store,
});

export default { dashboard, analytics };
