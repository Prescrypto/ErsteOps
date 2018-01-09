import find from 'lodash/fp/find';
import { mapState, mapMutations } from 'vuex';
import Loader from 'vue-spinner/src/ScaleLoader.vue';
import { SELECT_ADDRESS } from 'store/constants';

export default {
  name: 'addresses',
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
    ...mapState(['loading', 'patient', 'address']),
  },
  methods: {
    choose() {
      const address = find(a => a.id_address_id === this.current)(
        this.patient.addresses
      );
      this.selectAddress(address);
    },
    ...mapMutations({ selectAddress: SELECT_ADDRESS }),
  },
};
