import { mapState, mapMutations } from 'vuex';
import Loader from 'vue-spinner/src/ScaleLoader.vue';
import { UPDATE_COPAGO_AMOUNT } from 'store/constants';
import Treeselect from '@riophae/vue-treeselect';
import { TREE_DATA } from 'store/tree_data';

export default {
  name: 'patient',
  inject: ['$validator'],
  components: { Loader, Treeselect },
  data() {
    return {
      multiple: true,
      clearable: true,
      searchable: true,
      openOnClick: false,
      clearOnSelect: true,
      disableBranchNodes: true,
      options: TREE_DATA,
    };
  },
  computed: {
    // Remove this becase the plan is not included and the subscription type is begin keeped without translation on erste database
    // subscription() {
    //   var plan_type = (this.emergency.comment != null ? ' - Plan: ' + this.emergency.comment : ' N/A');
    //   return {
    //     company: 'Compañia' + plan_type,
    //     family: 'Familia' + plan_type,
    //     private: 'Privado' + plan_type,
    //   }[this.emergency.subscription_type];
    // },
    subscription() {
      return this.emergency.subscription_type;
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
