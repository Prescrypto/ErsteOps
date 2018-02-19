import { mapGetters } from 'vuex';

export default {
  name: 'analytics',
  computed: {
    ...mapGetters({
      emergencies: 'activeEmergencyCount',
      units: 'activeUnitsCount',
    }),
  },
};
