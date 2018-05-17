import find from 'lodash/fp/find';
import { mapActions, mapState } from 'vuex';
import Avatar from 'vue-avatar';

export default {
  name: 'units',
  components: { Avatar },
  mounted() {
    this.details(this.id);
  },
  computed: {
    ...mapState('unit', {
      unit(state) {
        return find(unit => unit.id === this.id)(state.units);
      },
    }),
    type() {
      return this.unit.unit_type
        ? {
            urgencias_avanzadas: 'Ambulancia de urgencias avanzadas económico',
            terapia_intensiva: 'Ambulancia de terapia intensiva económico',
            urgencias_basicas: 'Ambulancia de urgencias básicas económico',
            vehiculo_consulta_medica_domicilio:
              'Vehículos de consulta médica a domicilio, Económico',
          }[this.unit.unit_type]
        : 'Indefinido';
    },
  },
  methods: {
    ...mapActions('unit', ['details']),
  },
  props: ['id'],
};
