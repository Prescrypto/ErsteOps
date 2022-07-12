export default {
  name: 'AirWay',
  data: () => ({
    airway_type: [],
    other_airway: '',
    instructions: '',
    prev_elements: [],
    select_text: '',
    paperless: window.erste.paperless,
    selected: '',
    options: [
      { text: '', value: '' },
      { text: 'Manual', value: 'Manual' },
      { text: 'Orifaringea', value: 'Orifaringea' },
      { text: 'Endotraqueal', value: 'Endotraqueal' },
      { text: 'Nasofaringea', value: 'Nasofaringea' },
      { text: 'Ventilador', value: 'Ventilador' },
      { text: 'Aspiración', value: 'Aspiración' },
      { text: 'P.N l/min', value: 'P.N l/min' },
      { text: 'M.R l/min', value: 'M.R l/min' },
      { text: 'M.S l/min', value: 'M.S l/min' },
      { text: 'B.V.M l/min', value: 'B.V.M l/min' },
      { text: 'Otro', value: 'Otro' },
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
        // if (this.selected === 'Ninguna') {
        //   this.prev_elements = [];
        //   this.instructions = '';
        // }
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
