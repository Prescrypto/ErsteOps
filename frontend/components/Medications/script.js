export default {
  name: 'AirWay',
  data: () => ({
    // airway_type: [],
    // other_airway: '',
    // instructions: '',
    medicationType: '',
    medicationName: '',
    medicationDose: '',
    medicationHrs: '',
    prevElements: [],
    select_text: '',
    paperless: window.erste.paperless,
    selected: 'Ninguna',
    options: [
      { text: 'Ninguna', value: 'Ninguna' },
      { text: 'Hemoderivado-Solucion', value: 'Hemoderivado-Solucion' },
      { text: 'Hemoderivado-Hemoderivado', value: 'Hemoderivado-Hemoderivado' },
      {
        text: 'Cardiovascular-Desfibrilacion',
        value: 'Cardiovascular-Desfibrilacion',
      },
      {
        text: 'Cardiovascular-Cardioversion',
        value: 'Cardiovascular-Cardioversion',
      },
      { text: 'Farmacologico-Farmaco', value: 'Farmacologico-Farmaco' },
      { text: 'Farmacologico-Aminas', value: 'Farmacologico-Aminas' },
    ],
  }),
  methods: {
    async submit(e) {
      try {
        e.stopPropagation();
        e.preventDefault();
        // if (this.selected === 'Otro') {
        //   this.select_text = this.other_airway;
        // } else {
        //   this.select_text = this.selected;
        // }
        // if (this.selected === 'Ninguna') {
        //   this.prev_elements = [];
        //   this.instructions = '';
        // }
        if (
          this.selected === 'Hemoderivado-Solucion' ||
          this.selected === 'Hemoderivado-Hemoderivado'
        ) {
          this.medicationHrs = 0;
        }
        const medicationElement = {
          medication_type: this.selected,
          medication_name: this.medicationName,
          medication_dose: this.medicationDose,
          medication_hrs: this.medicationHrs,
        };
        this.prevElements.push(medicationElement);
        this.paperless.medications = this.prevElements;
      } catch (err) {
        this.$emit('error', err);
        this.$notify({
          text: `No se pudo agregar via aerea${err}`,
          type: 'error',
        });
      }
    }, // submit
    async eliminate(e, item) {
      try {
        e.stopPropagation();
        e.preventDefault();
        this.prevElements.splice(item, 1);
        this.paperless.medications = this.prevElements;
        // console.log(item);
      } catch (err) {
        this.$emit('error', err);
        this.$notify({
          text: `No se pudo eliminar ls medicación: ${err}`,
          type: 'error',
        });
      }
    }, // eliminate
  },
};
