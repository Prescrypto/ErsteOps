export default {
  name: 'AirWay',
  data: () => ({
    airway_type: [],
    other_airway: '',
    instructions: '',
    prev_elements: [],
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
        if (this.selected === 'Otro') {
          this.select_text = this.other_airway;
        } else {
          this.select_text = this.selected;
        }
        if (this.selected === 'Ninguna') {
          this.prev_elements = [];
          this.instructions = '';
        }
        const airwayElement = {
          airway_type: this.select_text,
          instruction: this.instructions,
        };
        this.prev_elements.push(airwayElement);
        this.paperless.airway = this.prev_elements;
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
        this.prev_elements.splice(item, 1);
        this.paperless.airway = this.prev_elements;
        // console.log(item);
      } catch (err) {
        this.$emit('error', err);
        this.$notify({
          text: `No se pudo eliminar via aerea${err}`,
          type: 'error',
        });
      }
    }, // eliminate
  },
};
