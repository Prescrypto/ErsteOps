import 'filters/time-since';
import ReconnectingWebSocket from 'reconnecting-websocket';
import { mapState, mapActions, mapMutations } from 'vuex';
import { ws } from 'utils/url';
import http from 'utils/http';
import { MODAL_CHANGE_TAB, REMOVE_INCIDENT_ON_NOTIFICATION } from 'store/constants';

// Connect to WebSocket
const socket = new ReconnectingWebSocket(`${ws}/notify/emergency/`);

// Initialize empty data store
const { incidents } = window.erste;
let emergencies = incidents.map(i => ({ id: i.pk, ...i.fields })) || [];
const store = { emergencies };

// helper function for remove element for array
function removeElement(array, element_id) {
    // compare ID given on array
    // TODO add remove option on emergency
    return array.filter(e => e['id'] !== element_id);
}

// Append to emergencies array when receiving new data
socket.onmessage = message => {
  const dataTemp = JSON.parse(message.data);
  const data = JSON.parse(dataTemp);
  if(data["is_active"]){
    emergencies.push(data);
  }else{
    // TODO made this work, remove emergency if was changed to is_active = False
    console.log("Remove if necesary");
    console.log(emergencies);
    emergencies = removeElement(emergencies, data["id"]);
    console.log("After remove");
    console.log(emergencies)
    console.log(`New emergency notification but not is_active True`);
    // end TODO
  }
};

export default {
  name: 'dashboard-log',
  data: () => ({
    ...store,
    now: Date.now()
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
      $('#emergency-'+id).toggle();
      // stop timer
      http.get(`/emergency/ajax/end/${id}/`);
    },
    // maps the search action from the store to the component
    ...mapActions(['emergency']),
  },
};
