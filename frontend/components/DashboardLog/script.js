import 'filters/time-since';
import ReconnectingWebSocket from 'reconnecting-websocket';
import { mapState, mapActions, mapMutations } from 'vuex';
import {
  findIndex,
  filter,
  sortBy,
  map,
  flow,
  reverse,
  uniqBy,
} from 'lodash/fp';
import { ws } from 'utils/url';
import http from 'utils/http';
import { MODAL_CHANGE_TAB } from 'store/constants';

// Connect to WebSocket
const socket = new ReconnectingWebSocket(`${ws}/notify/emergency/`);

// Initialize empty data store
const { incidents } = window.erste;

// Add emergencies and sort by start time
let emergencies =
  flow(
    map(emergency => ({ id: emergency.pk, ...emergency.fields })),
    sortBy(emergency => new Date(emergency.start_time).getTime()),
    reverse
  )(incidents) || [];

// Append to emergencies array when receiving new data
socket.onmessage = message => {
  const dataTemp = JSON.parse(message.data);
  const data = JSON.parse(dataTemp);
  const { id } = data;

  // add emergency
  const updateId = findIndex(emergency => emergency.id === id)(emergencies);
  if (updateId >= 0) {
    emergencies[updateId] = { ...emergencies[updateId], ...data };
  } else {
    emergencies.push(data);
  }

  // keep only active emergencies
  emergencies = flow(
    filter(emergency => emergency.is_active),
    uniqBy('id'),
    sortBy(emergency => new Date(emergency.start_time).getTime()),
    reverse
  )(emergencies);
};

export default {
  name: 'dashboard-log',
  data: () => ({
    emergencies,
    now: Date.now(),
  }),
  mounted() {
    setInterval(() => {
      this.$data.now = Date.now();
    }, 1000);
  },
  computed: {
    ...mapState({
      // for hiding the spinner
      loading: 'loading',
      // server results array
      current: 'emergency',
    }),
  },
  methods: {
    ...mapMutations({
      changeTab: MODAL_CHANGE_TAB,
    }),
    // lookup emergency by id
    populate(id) {
      this.emergency(id);
      this.changeTab('patient');
      window.Erste.modal.show();
    },
    // stops the timer
    stop(e, id) {
      // prevet modal from opening
      e.stopPropagation();
      // stop timer
      http.get(`/emergency/ajax/end/${id}/`);
      // remove from active emergencies
      this.emergencies = filter(emergency => emergency.id !== id)(
        this.emergencies
      );
    },
    // maps the search action from the store to the component
    ...mapActions(['emergency']),
  },
};
