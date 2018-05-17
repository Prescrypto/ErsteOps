import UnitDetails from 'components/UnitDetails';

export default {
  name: 'unit',
  components: { UnitDetails },
  computed: {
    label() {
      return this.data.identifier;
    },
  },
  props: {
    data: {
      default: {},
      type: Object,
    },
    tooltip: {
      default: 'top',
      type: String,
    },
  },
};
