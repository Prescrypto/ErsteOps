import { mapState } from 'vuex';
import Loader from 'vue-spinner/src/ScaleLoader.vue';

export default {
  name: 'patient',
  components: { Loader },
  computed: {
    subscription() {
      return {
        company: 'Compañia',
        family: 'Familia',
        private: 'Privado',
      }[this.emergency.subscription_type];
    },
    ...mapState(['loading', 'emergency']),
    source() {
      return this.emergency;
    },
  },
};
