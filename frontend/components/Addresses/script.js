import find from 'lodash/fp/find';
import pick from 'lodash/fp/pick';
import { mapState, mapMutations } from 'vuex';
import Loader from 'vue-spinner/src/ScaleLoader.vue';
import { SELECT_ADDRESS } from 'store/constants';

export default {
  name: 'addresses',
  inject: ['$validator'],
  components: { Loader },
  beforeUpdate() {
    this.current = 0;
    this.selectAddress(this.finalAddress);
  },
  data() {
    return {
      current: 0,
    };
  },
  computed: {
    finalAddress() {
      return this.emergency.id
        ? pick([
            'address_and_street',
            'address_between',
            'address_col',
            'address_county',
            'address_extra',
            'address_front',
            'address_instructions',
            'address_notes',
            'address_ref',
            'address_street',
            'address_zip_code',
          ])(this.emergency)
        : this.address;
    },
    ...mapState(['loading', 'emergency']),
    ...mapState({ address: state => state.modal.address }),
  },
  methods: {
    choose() {
      const address = find(a => a.address_id === this.current)(
        this.emergency.addresses
      );
      this.selectAddress(address);
    },
    ...mapMutations({ selectAddress: SELECT_ADDRESS }),
  },
};
