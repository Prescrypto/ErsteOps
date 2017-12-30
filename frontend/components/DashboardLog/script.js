import init from 'utils/init';
import ReconnectingWebSocket from 'reconnecting-websocket';
import { ws } from 'utils/url';

// Initialize Vue globals
init();

// Connect to WebSocket
const socket = new ReconnectingWebSocket(`${ws}/notify/emergency/`);

// Initialize empty data store
const emergencies = window.erste.incidents.map(i => i.fields) || [];
const store = { emergencies };

// Append to emergencies array when receiving new data
socket.onmessage = message => {
  const dataTemp = JSON.parse(message.data);
  const data = JSON.parse(dataTemp);
  emergencies.push(data);
};

export default {
  name: 'dashboard-log',
  data: () => store,
};
