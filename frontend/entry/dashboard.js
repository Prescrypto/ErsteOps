import Vue from 'vue';
import Notifications from 'vue-notification';
import VueClipboard from 'vue-clipboard2';
import VTooltip from 'v-tooltip';
import DashboardLog from 'components/DashboardLog';
import Analytics from 'components/Analytics';
import store from 'store';

Vue.use(VTooltip);
Vue.use(Notifications);
Vue.use(VueClipboard);

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
