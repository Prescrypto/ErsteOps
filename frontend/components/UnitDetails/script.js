import { mapActions } from 'vuex';

export default {
  name: 'unit-details',
  data: () => ({
    unitId: 1,
  }),
  mounted() {
    this.details(this.unitId);
  },
  methods: {
    ...mapActions('unit', ['details']),
  },
};
