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
      openOnClick: false,
      clearOnSelect: true,
      disableBranchNodes: true,
      options: [
        {
          id: 'Convulsiones',
          label: 'Convulsiones',
          children: [
            {
              id: 'Esta convulsionando ahora',
              label: 'Esta convulsionando ahora',
              children: [
                {
                  id: 'G1',
                  label: 'Grado 1',
                },
              ],
            },
            {
              id: 'No esta convulsionando ahora',
              label: 'No esta convulsionando ahora',
              children: [
                {
                  id: 'No esta conciente',
                  label: 'No esta conciente',
                  children: [
                    {
                      id: 'G1',
                      label: 'Grado 1',
                    },
                  ],
                },
                {
                  id: 'Esta consciente',
                  label: 'Esta consciente',
                  children: [
                    {
                      id: 'Respira mal',
                      label: 'Respira mal',
                      children: [
                        {
                          id: 'G2',
                          label: 'Grado 2',
                        },
                      ],
                    },
                    {
                      id: 'Respira bien',
                      label: 'Respira bien',
                      children: [
                        {
                          id: 'G3',
                          label: 'Grado 3',
                        },
                      ],
                    },
                  ],
                },
              ],
            },
          ],
        },
        {
          id: 'Accidente Vehicular',
          label: 'Accidente Vehicular',
          children: [
            {
              id: 'G1',
              label: 'Grado 1',
            },
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
