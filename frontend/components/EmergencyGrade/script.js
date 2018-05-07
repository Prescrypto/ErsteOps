import find from 'lodash/fp/find';
import { mapActions } from 'vuex';

export default {
  name: 'emergency-grade',
  data: () => ({
    hover: 0,
    justification: '',
    grades: [
      {
        name: 'G3',
        weight: 1,
        description: 'Consulta Médica de Primer Contacto',
      },
      { name: 'G2', weight: 2, description: 'Urgencia Médica' },
      { name: 'G1', weight: 3, description: 'Emergencia Médica' },
    ],
  }),
  computed: {
    type() {
      return this.emergency.grade_type;
    },
  },
  methods: {
    ...mapActions('finalGrade', ['setFinalGrade']),
    isActive({ name, weight }) {
      const isCurrent = name === this.type;

      const grade = find(g => this.type === g.name)(this.grades) || {};
      const isBelowCurrent = grade.weight > weight;
      const isBelowHovered = this.hover > weight;

      return isCurrent || isBelowCurrent || isBelowHovered;
    },
    async setGrade(e, { name }) {
      try {
        e.stopPropagation();
        const response = await this.setFinalGrade({
          id: this.emergency.id,
          attention_final_grade: name,
          attention_justification: this.justification,
        });
        this.$emit('graded', response);

        this.$notify({
          text: 'Se cambio el grado de la emergencia existosamente',
          type: 'success',
        });
      } catch (err) {
        this.$emit('error', err);
        this.$notify({
          text: 'No se pudo cambiar el grado de la emergencia',
          type: 'error',
        });
      }
    },
    setHover(weight) {
      this.hover = weight;
    },
    unsetHover() {
      this.hover = 0;
    },
  },
  props: ['emergency'],
};
