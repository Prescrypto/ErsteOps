import Vue from 'vue';
import ReconnectingWebSocket from 'reconnecting-websocket';
import { ws } from 'utils/url';
import init from 'utils/init';

// Initialize Vue globals
init();

// Connect to WebSocket
const socket = new ReconnectingWebSocket(`${ws}/notify/emergency/`);

// Initialize empty data store
const emergencies = [];
const store = { emergencies };

// Append to emergencies array when receiving new data
socket.onmessage = message => {
  const dataTemp = JSON.parse(message.data);
  const data = JSON.parse(dataTemp);
  emergencies.push(data);
};

// Initialize Vue component from HTML
const root = new Vue({
  el: '#dashboard-log',
  delimiters: ['<%', '%>'],
  data: store,
});

export default root;
