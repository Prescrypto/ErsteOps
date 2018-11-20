// import { mapState, mapMutations } from 'vuex';
import Loader from 'vue-spinner/src/ScaleLoader.vue';
// import { UPDATE_COPAGO_AMOUNT } from 'store/constants';

export default {
  name: 'timers',
  inject: ['$validator'],
  components: { Loader },
};
