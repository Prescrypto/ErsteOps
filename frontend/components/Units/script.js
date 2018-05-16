import find from 'lodash/fp/find';
import { mapState, mapActions, mapMutations, mapGetters } from 'vuex';
import Loader from 'vue-spinner/src/ScaleLoader.vue';
import UnitDetails from 'components/UnitDetails';
import {
  MODAL_UNITS_ADD,
  MODAL_UNITS_REMOVE,
  MODAL_UNITS_SET,
} from 'store/constants';

export default {
  name: 'units',
  components: { Loader, UnitDetails },
  data: () => ({
    hover: null,
  }),
  mounted() {
    this.getUnits();
  },
  computed: {
    ...mapState(['loading', 'units', 'selected', 'emergency']),
    ...mapGetters(['combinedUnits']),
  },
  filters: {
    description: type =>
      ({
        undefined: 'Indefinido',
        terapia_intensiva: 'Ambulancia de terapia intensiva económico',
        vehiculo_consulta_medica_domicilio:
          'Vehículos de consulta médica a domicilio, Económico',
        urgencias_avanzadas: 'Ambulancia de urgencias avanzadas económico',
        urgencias_basicas: 'Ambulancia de urgencias básicas económico',
      }[type]),
  },
  methods: {
    add(e, unit) {
      e.stopPropagation();
      this.addUnit(unit);
    },
    remove(e, unit) {
      e.stopPropagation();
      this.removeUnit(unit);
    },
    isSelected(id) {
      return find(u => id === u.id)(this.combinedUnits);
    },
    setHover(id) {
      this.hover = id;
    },
    unsetHover() {
      this.hover = null;
    },
    ...mapMutations({
      addUnit: MODAL_UNITS_ADD,
      removeUnit: MODAL_UNITS_REMOVE,
      setUnits: MODAL_UNITS_SET,
    }),
    ...mapActions({ getUnits: 'units' }),
  },
};
