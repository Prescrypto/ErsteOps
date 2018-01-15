import Vue from 'vue';
import { format } from 'date-fns';

/**
 * Format date according to format string
 *
 * @param {Date|number} timestamp Javascript date or UNIX timestamp
 * @param {string} fm Optional format string
 * @returns {string} Formatted date string
 */
Vue.filter('datetime', (timestamp, fmt = 'hh:mm:ss A') => {
  if (!timestamp) return '';
  return format(timestamp, fmt);
});
