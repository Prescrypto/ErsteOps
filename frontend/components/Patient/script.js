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
      }[this.patient.id_subscription_type];
    },

    ...mapState({
      // loading is for hiding the spinner
      loading: 'loading',
      // suggestions is the server results array
      patient: 'patient',
    }),
  },
};
