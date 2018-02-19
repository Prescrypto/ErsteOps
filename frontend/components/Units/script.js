import find from 'lodash/fp/find';
import { mapState, mapActions, mapMutations, mapGetters } from 'vuex';
import Loader from 'vue-spinner/src/ScaleLoader.vue';
import {
  MODAL_UNITS_ADD,
  MODAL_UNITS_REMOVE,
  MODAL_UNITS_SET,
} from 'store/constants';

export default {
  name: 'units',
  components: { Loader },
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
        terapia_intensiva: 'Ambulancia de terapia intensiva',
        vehiculo_consulta_medica_domicilio:
          'Vehiculo consulta medica a domicilio',
        urgencias_avanzadas: 'Ambulancia de urgencias avanzadas',
        urgencias_basicas: 'Ambulancia de urgencias básicas',
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
    ...mapMutations({
      addUnit: MODAL_UNITS_ADD,
      removeUnit: MODAL_UNITS_REMOVE,
      setUnits: MODAL_UNITS_SET,
    }),
    ...mapActions({ getUnits: 'units' }),
  },
};
