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
          label: '(Adulto) AHOGADOS POR INMERSION',
          state: {
            opened: 'true',
          },
          id: '1-1000000',
          children: [
            {
              label: '    No esta consciente [Grado : 1]',
              id: '1-1100000',
            },
            {
              label: '    Esta consciente',
              children: [
                {
                  label: '        Respira bien [Grado : 2]',
                  id: '1-1210000',
                },
                {
                  label: '        No Respira bien [Grado : 1]',
                  id: '1-1220000',
                },
              ],
              id: '1-1200000',
            },
          ],
        },
        {
          label: '(Adulto) ALTERACION DE LA AUDICION [Grado : 3]',
          state: {
            opened: 'true',
          },
          id: '1-2000000',
        },
        {
          label: '(Adulto) ACCIDENTE VEHICULAR [Grado : 1]',
          state: {
            opened: 'true',
          },
          id: '1-4000000',
        },
        {
          label: '(Adulto) ARRITMIAS [Nota : (REALIZAR ECG)]',
          state: {
            opened: 'true',
          },
          id: '1-5000000',
          children: [
            {
              label: '    No esta consciente [Grado : 1]',
              id: '1-5100000',
            },
            {
              label: '    Esta consciente',
              children: [
                {
                  label: '        Tiene dolor de pecho [Grado : 1]',
                  id: '1-5210000',
                },
                {
                  label: '        No tiene dolor de pecho [Grado : 2]',
                  id: '1-5220000',
                },
              ],
              id: '1-5200000',
            },
          ],
        },
        {
          label: '(Adulto) CONSTIPACION [Grado : 3]',
          state: {
            opened: 'true',
          },
          id: '1-7000000',
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
