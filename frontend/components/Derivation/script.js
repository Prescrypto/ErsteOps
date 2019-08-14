import { mapState } from 'vuex';
import Loader from 'vue-spinner/src/ScaleLoader.vue';

export default {
  name: 'emergency-derivation',
  props: ['emergency'],
  components: { Loader },
  computed: {
    ...mapState(['loading', 'emergency']),
    source() {
      return this.emergency;
    },
    emergency_link() {
      const eName = `/admin/emergency/emergency/${
        this.emergency.id
      }/change/#/tab/module_5/`;
      return eName;
    },
  },
};
