import 'filters/time-since';
import { mapState, mapActions, mapMutations, mapGetters } from 'vuex';
import { MODAL_CHANGE_TAB, EMERGENCY_TEXT_CLEAR } from 'store/constants';
import EmergencyGrade from 'components/EmergencyGrade';

export default {
  name: 'dashboard-log',
  data: () => ({
    now: Date.now(),
  }),
  components: { EmergencyGrade },
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
      // serialized emergency text
      emergencyText: 'emergencyText',
    }),
    ...mapGetters({
      emergencies: 'sortActiveEmergencies',
    }),
  },
  methods: {
    ...mapMutations({
      changeTab: MODAL_CHANGE_TAB,
      clearEmergencyText: EMERGENCY_TEXT_CLEAR,
    }),
    // lookup emergency by id
    populate(id) {
      this.emergency(id);
      this.changeTab('patient');
      window.Erste.modal.show();
    },
    // stops the timer
    stop(e, id) {
      // prevent modal from opening
      e.stopPropagation();
      // stop timer
      this.stopTimer(id);
    },
    // copy serialized emergency to clipboard
    text(e, id) {
      // prevent modal from opening
      e.stopPropagation();
      // fetch emergency text
      this.emergencyDetails(id);
    },
    selectText(e) {
      e.currentTarget.select();
      e.currentTarget.setSelectionRange(0, e.currentTarget.value.length);
    },
    onCopy() {
      this.clearEmergencyText();
      this.$notify({
        text: 'Se ha copiado el incidente al portapapeles.',
        type: 'success',
      });
    },
    onCopyError() {
      this.$notify({
        text: 'No se pudo copiar el incidente al portapapeles',
        type: 'error',
      });
    },
    // maps the search action from the store to the component
    ...mapActions(['emergency', 'stopTimer', 'emergencyDetails']),
  },
};
