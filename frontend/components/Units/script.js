import { mapState, mapActions } from 'vuex';
import Loader from 'vue-spinner/src/ScaleLoader.vue';

export default {
  name: 'units',
  components: { Loader },
  mounted() {
    this.getUnits();
  },
  data() {
    return {
      current: 0,
    };
  },
  computed: {
    ...mapState(['loading', 'units']),
  },
  methods: {
    choose() {},
    ...mapActions({ getUnits: 'units' }),
  },
};
