export default {
  name: 'PhysicalExploration',
  data: () => ({
    pe_time: '',
    pe_heart_rate: '',
    pe_respiratory_rate: '',
    pe_blood_pressure: '',
    pe_temperature: '',
    pe_oxygen_saturation: '',
    pe_glucometry: '',
    pe_glassgow: '',
    peElement: '',
    paperless: window.erste.paperless,
    prev_elements: [],
  }),
  methods: {
    async submit(e) {
      try {
        e.stopPropagation();
        e.preventDefault();
        const peElement = {
          time: this.pe_time,
          heart_rate: this.pe_heart_rate,
          respiratory_rate: this.pe_respiratory_rate,
          blood_pressure: this.pe_blood_pressure,
          temperature: this.pe_temperature,
          oxygen_saturation: this.pe_oxygen_saturation,
          glucometry: this.pe_glucometry,
          glassgow: this.pe_glassgow,
        };
        this.prev_elements.push(peElement);
        this.paperless.physical_exploration = this.prev_elements;
      } catch (err) {
        this.$emit('error', err);
        this.$notify({
          text: `No se pudo agregar exploracion fisica${err}`,
          type: 'error',
        });
      }
    },
  },
};
