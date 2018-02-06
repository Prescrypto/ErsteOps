import { mapGetters } from 'vuex';

export default {
  name: 'analytics',
  data: () => ({
    units: 0,
  }),
  computed: {
    ...mapGetters({
      emergencies: 'activeEmergencyCount',
    }),
  },
};
