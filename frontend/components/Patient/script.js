import { mapState, mapMutations } from 'vuex';
import Loader from 'vue-spinner/src/ScaleLoader.vue';
import { UPDATE_COPAGO_AMOUNT } from 'store/constants';
import Treeselect from '@riophae/vue-treeselect';

export default {
  name: 'patient',
  inject: ['$validator'],
  components: { Loader, Treeselect },
  data() {
    return {
      multiple: true,
      clearable: true,
      searchable: true,
      openOnClick: true,
      clearOnSelect: true,
      options: [
        {
          id: 'bikes',
          label: 'Bikes',
          children: [
            // // array of bike objss
          ],
        },
        {
          id: 'Cars',
          label: 'Cars',
          children: [
            // array of car objs
          ],
        },
      ],
    };
  },
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
