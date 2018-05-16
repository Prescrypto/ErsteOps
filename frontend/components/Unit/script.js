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
    setHover() {
      this.hover = true;
    },
    unsetHover() {
      this.hover = false;
    },
  },
  props: ['data'],
};
