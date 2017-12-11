import Vue from 'vue';
import { format } from 'date-fns';

// Filters
Vue.filter('datetime', (timestamp, fmt = 'hh:mm:ss A') => {
  if (!timestamp) return '';
  return format(timestamp, fmt);
});

// Dashboard table component
const root = new Vue({
  el: '#dashboard-root',
  delimiters: ['<%', '%>'],
  data: {
    emergencies: [
      {
        id: 'someuuid',
        is_active: true,
        odoo_client: 'Fulano DeTal',
        grade_type: 'Severe',
        unit: {
          // all: ['Alpha', 'Beta']
        },
        start_time: Date.now(),
      },
    ],
  },
});

export default root;
