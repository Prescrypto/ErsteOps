import find from 'lodash/fp/find';
import { mapActions } from 'vuex';

export default {
  name: 'emergency-grade',
  data: () => ({
    hover: 0,
    finalGrade: null,
    finalGradeError: null,
    justification: null,
    grades: [
      {
        name: 'G3',
        weight: 1,
        description: 'Consulta Médica de Primer Contacto',
      },
      { name: 'G2', weight: 2, description: 'Urgencia Médica' },
      { name: 'G1', weight: 3, description: 'Emergencia Médica' },
      { name: 'G0', weight: 0, description: 'Sin Definir' },
    ],
  }),
  computed: {
    type() {
      return this.emergency.grade_type;
    },
    isValid() {
      return this.finalGrade && this.justification;
    },
  },
  methods: {
    ...mapActions('finalGrade', ['setFinalGrade']),
    isActive({ name, weight }) {
      const isCurrent = name === this.type;
      const isGraded = name === (this.finalGrade || {}).name;

      const grade =
        this.finalGrade || find(g => this.type === g.name)(this.grades) || {};
      const isBelowCurrent = grade.weight > weight;
      const isBelowHovered = this.hover > weight;

      return isGraded || isCurrent || isBelowCurrent || isBelowHovered;
    },
    setGrade(e, grade) {
      e.stopPropagation();
      e.preventDefault();

      const current = find(g => this.type === g.name)(this.grades);

      if (current.weight === 0 || current.weight >= grade.weight) {
        this.finalGrade = grade;
        this.finalGradeError = null;
      } else {
        this.finalGrade = null;
        this.finalGradeError = 'El grado debe ser de igual o menor urgencia';
      }
    },
    async submit(e) {
      try {
        e.stopPropagation();
        e.preventDefault();
        const response = await this.setFinalGrade({
          id: this.emergency.id,
          attention_final_grade: this.finalGrade.name,
          attention_justification: this.justification,
        });
        this.$emit('graded', response);

        this.$notify({
          text: 'Se cambio el grado del auxilio existosamente',
          type: 'success',
        });
      } catch (err) {
        this.$emit('error', err);
        this.$notify({
          text: 'No se pudo cambiar el grado del auxilio',
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
  $_veeValidate: {
    validator: 'new',
  },
};
