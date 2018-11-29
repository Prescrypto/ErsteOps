import { mapActions } from 'vuex';
// import find from 'lodash/fp/find';

export default {
  name: 'dashboard-timers',
  props: ['emergency'],
  data: () => ({
    timerPicked: null,
    enableRadio: false,
  }),

  computed: {
    isValid() {
      return this.timerPicked != null;
    },

    isValidUnitDispatchedTime() {
      const minimalStartTime = Intl.DateTimeFormat('en-US', {
        year: 'numeric',
        month: 'short',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
      }).format(new Date(Date.parse(this.emergency.start_time)).setSeconds(0));
      const minimalUnitDispatchedTime = Intl.DateTimeFormat('en-US', {
        year: 'numeric',
        month: 'short',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
      }).format(
        new Date(Date.parse(this.emergency.unit_dispatched_time)).setSeconds(0)
      );
      return minimalStartTime === minimalUnitDispatchedTime;
    },

    isValidArrivalTime() {
      const minimalStartTime = Intl.DateTimeFormat('en-US', {
        year: 'numeric',
        month: 'short',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
      }).format(new Date(Date.parse(this.emergency.start_time)).setSeconds(0));
      const minimalArrivalTime = Intl.DateTimeFormat('en-US', {
        year: 'numeric',
        month: 'short',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
      }).format(
        new Date(Date.parse(this.emergency.arrival_time)).setSeconds(0)
      );
      return minimalStartTime === minimalArrivalTime;
    },

    isValidDerivationTime() {
      const minimalStartTime = Intl.DateTimeFormat('en-US', {
        year: 'numeric',
        month: 'short',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
      }).format(new Date(Date.parse(this.emergency.start_time)).setSeconds(0));
      const minimalDerivationTime = Intl.DateTimeFormat('en-US', {
        year: 'numeric',
        month: 'short',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
      }).format(
        new Date(Date.parse(this.emergency.derivation_time)).setSeconds(0)
      );
      return minimalStartTime === minimalDerivationTime;
    },

    isValidPatientArrivalTime() {
      const minimalStartTime = Intl.DateTimeFormat('en-US', {
        year: 'numeric',
        month: 'short',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
      }).format(new Date(Date.parse(this.emergency.start_time)).setSeconds(0));
      const minimalPatientArrivalTime = Intl.DateTimeFormat('en-US', {
        year: 'numeric',
        month: 'short',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
      }).format(
        new Date(Date.parse(this.emergency.patient_arrival)).setSeconds(0)
      );
      return minimalStartTime === minimalPatientArrivalTime;
    },
  },
  methods: {
    ...mapActions('updateTimer', ['setUpdateTimer']),

    show_timers() {
      return true;
    },

    async submit(e) {
      try {
        e.stopPropagation();
        e.preventDefault();

        const response = await this.setUpdateTimer({
          id: this.emergency.id,
          timer_type: this.timerPicked,
        });
        this.$emit('updatetimer', response);

        this.$notify({
          text: `Se actualizo el timer del auxilio existosamente ${
            this.emergency.id
          }`,
          type: 'success',
        });
      } catch (err) {
        this.$emit('error', err);
        this.$notify({
          text: `No se pudo actualizar el timer del auxilio${err}`,
          type: 'error',
        });
      }
    },
  },
};
