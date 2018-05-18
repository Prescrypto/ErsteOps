import { mapState } from 'vuex';
import Loader from 'vue-spinner/src/ScaleLoader.vue';

export default {
  name: 'addresses',
  inject: ['$validator'],
  components: { Loader },
  beforeUpdate() {
    this.current = 0;
  },
  data() {
    return {
      current: 0,
    };
  },
  computed: {
    ...mapState(['loading', 'emergency']),
  },
};
