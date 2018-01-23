import Vue from 'vue';
import {
  parse,
  differenceInHours,
  differenceInMinutes,
  differenceInSeconds,
  addHours,
  addMinutes,
} from 'date-fns';

function pad(n, width = 2, z = 0) {
  n = n + ''; // eslint-disable-line
  return n.length >= width ? n : new Array(width - n.length + 1).join(z) + n;
}

/**
 * Show time since given date
 *
 * @param {Date|number} timestamp Javascript date or UNIX timestamp
 * @param {string} fm Optional format string
 * @returns {string} Formatted date string
 */
Vue.filter('timeSince', (timestamp, now) => {
  if (!timestamp) return '';
  const delta = {};
  let time = parse(timestamp);

  delta.hours = differenceInHours(now, time);
  time = addHours(time, delta.hours);

  delta.minutes = differenceInMinutes(now, time);
  time = addMinutes(time, delta.minutes);

  delta.seconds = differenceInSeconds(now, time);

  const { hours, minutes, seconds } = delta;
  return `${pad(hours)}:${pad(minutes)}:${pad(seconds)}`;
});
