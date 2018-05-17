import UnitDetails from 'components/UnitDetails';

export default {
  name: 'unit',
  components: { UnitDetails },
  data: () => ({
    hover: false,
  }),
  computed: {
    label() {
      return this.data.identifier;
    },
  },
  methods: {
    handleShow() {
      this.hover = true;
    },
    handleHide() {
      this.hover = false;
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
