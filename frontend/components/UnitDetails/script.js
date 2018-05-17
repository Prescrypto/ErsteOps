import { mapActions } from 'vuex';

export default {
  name: 'units',
  // this.details(this.current);
  computed: {
    id() {
      return this.current.id;
    },
  },
  methods: {
    ...mapActions('unit', ['details']),
  },
  props: ['current'],
};
