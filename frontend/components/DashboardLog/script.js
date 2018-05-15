import 'filters/time-since';
import find from 'lodash/fp/find';
import { mapState, mapActions, mapMutations, mapGetters } from 'vuex';
import { MODAL_CHANGE_TAB, EMERGENCY_TEXT_CLEAR } from 'store/constants';
import EmergencyGrade from 'components/EmergencyGrade';

export default {
  name: 'dashboard-log',
  data: () => ({
    now: Date.now(),
    stopped: null,
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
    async stop(e, id) {
      // prevent modal from opening
      e.stopPropagation();

      // set stop semaphore
      this.stopped = id;

      // stop timer and reset semaphore is tooltip skipped
      if (!this.showGradeTooltip(id)) {
        try {
          await this.stopTimer(id);
          this.stopped = null;

          this.$notify({
            text: 'Se ha finalizado la emergencia exitosamente.',
            type: 'success',
          });
        } catch (err) {
          this.$notify({
            text: 'Hubo un error al finalizar la emergencia.',
            type: 'error',
          });
        }
      }
    },
    graded(id/* , data */) {
      this.stopTimer(id);
    },
    gradedError() {
      this.stopped = null;
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
    showGradeTooltip(id) {
      const isStopped = id === this.stopped;

      const emergency = find(e => id === e.id)(this.emergencies);
      const isNotMostSevere = emergency.grade_type !== 'G1';

      return isStopped && isNotMostSevere;
    },
    // maps the search action from the store to the component
    ...mapActions(['emergency', 'stopTimer', 'emergencyDetails']),
  },
};
