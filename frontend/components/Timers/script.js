import { mapState, mapMutations } from 'vuex';
import Loader from 'vue-spinner/src/ScaleLoader.vue';
import { UPDATE_COPAGO_AMOUNT } from 'store/constants';
import { Datetime } from 'vue-datetime';
import 'vue-datetime/dist/vue-datetime.css';

export default {
  name: 'timers',
  inject: ['$validator'],
  components: { Loader, Datetime },
  computed: {
    source() {
      return this.emergency;
    },
  },
  ...mapState(['loading', 'emergency']),
  methods: {
    ...mapMutations({ updateCopago: UPDATE_COPAGO_AMOUNT }),
  },
};
