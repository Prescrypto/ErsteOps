import { mapActions } from 'vuex';

export default {
  name: 'units',
  // this.details(this.current);
  methods: {
    ...mapActions('unit', ['details']),
  },
  props: ['current'],
};
