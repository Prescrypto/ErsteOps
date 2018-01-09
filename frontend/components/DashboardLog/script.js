import init from 'utils/init';
import ReconnectingWebSocket from 'reconnecting-websocket';
import { mapState, mapActions } from 'vuex';
import { ws } from 'utils/url';

// Initialize Vue globals
init();

// Connect to WebSocket
const socket = new ReconnectingWebSocket(`${ws}/notify/emergency/`);

// Initialize empty data store
const { incidents } = window.erste;
const emergencies = incidents.map(i => ({ id: i.pk, ...i.fields })) || [];
const store = { emergencies };

// Append to emergencies array when receiving new data
socket.onmessage = message => {
  const dataTemp = JSON.parse(message.data);
  const data = JSON.parse(dataTemp);
  emergencies.push(data);
};

export default {
  name: 'dashboard-log',
  // preload with data from backend
  data: () => store,
  computed: {
    ...mapState({
      // for hiding the spinner
      loading: 'loading',
      // server results array
      current: 'emergency',
    }),
  },
  methods: {
    // lookup emergency by id
    populate(id) {
      this.emergency(id);
    },
    // maps the search action from the store to the component
    ...mapActions(['emergency']),
  },
};
