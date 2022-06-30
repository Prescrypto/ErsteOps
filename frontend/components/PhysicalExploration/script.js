export default {
  name: 'PhysicalExploration',
  data: () => ({
    peTime: '',
    peHeartRate: '',
    peRespiratoryRate: '',
    peBloodPressure: '',
    peTemperature: '',
    peOxygenSaturation: '',
    peGlucometry: '',
    peGlassgowFinal: '',
    peGlassgowMotor: '',
    peGlassgowOcular: '',
    peGlassgowVerbal: '',
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
          time: this.peTime,
          heart_rate: this.peHeartRate,
          respiratory_rate: this.peRespiratoryRate,
          blood_pressure: this.peBloodPressure,
          temperature: this.peTemperature,
          oxygen_saturation: this.peOxygenSaturation,
          glucometry: this.peGlucometry,
          glassgow_motor: this.peGlassgowMotor,
          glassgow_ocular: this.peGlassgowOcular,
          glassgow_verbal: this.peGlassgowVerbal,
          glassgow_total:
            this.peGlassgowMotor +
            this.peGlassgowOcular +
            this.peGlassgowVerbal,
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
