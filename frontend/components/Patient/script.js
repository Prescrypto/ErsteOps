import { mapState, mapMutations } from 'vuex';
import Loader from 'vue-spinner/src/ScaleLoader.vue';
import { UPDATE_COPAGO_AMOUNT } from 'store/constants';

export default {
  name: 'patient',
  inject: ['$validator'],
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
    copago: {
      get() {
        return this.emergency.copago_amount / 100;
      },
      set(value) {
        this.updateCopago(value);
      },
    },
  },
  methods: {
    ...mapMutations({ updateCopago: UPDATE_COPAGO_AMOUNT }),
  },
};
