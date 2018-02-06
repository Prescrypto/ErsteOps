import 'filters/time-since';
import { mapState, mapActions, mapMutations, mapGetters } from 'vuex';
import { MODAL_CHANGE_TAB } from 'store/constants';

export default {
  name: 'dashboard-log',
  data: () => ({
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
    ...mapGetters({
      emergencies: 'sortActiveEmergencies',
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
      this.stopTimer(id);
    },
    // maps the search action from the store to the component
    ...mapActions(['emergency', 'stopTimer']),
  },
};
