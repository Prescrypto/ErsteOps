// import { VueSignaturePad } from 'vue-signature-pad';

export default {
  name: 'SignatureMedic',
  // data: () => ({
  //   options: {
  //     penColor: "#c0f",
  //   },
  // }),
  // methods: {
  //   undo() {
  //     this.$refs.signaturePad.undoSignature();
  //   },
  //   save() {
  //     const { isEmpty, data } = this.$refs.signaturePad.saveSignature();

  //     alert("Open DevTools see the save data.");
  //     console.log(isEmpty);
  //     console.log(data);
  //   },
  //   change() {
  //     this.options = {
  //       penColor: "#00f",
  //     };
  //   },
  //   resume() {
  //     this.options = {
  //       penColor: "#c0f",
  //     };
  //   },
  // },
  //   components: {
  //   VueSignaturePad
  // },
  data: () => ({
    paperless: window.erste.paperless,
  }),
  methods: {
    async undo(e) {
      e.preventDefault();
      e.stopPropagation();
      this.$refs.signaturePad.undoSignature();
    },
    async save(e) {
      e.preventDefault();
      e.stopPropagation();

      const { isEmpty, data } = this.$refs.signaturePad.saveSignature();
      console.log(isEmpty);
      console.log(data);
      this.paperless.signature_medic = data;
      console.log(this.paperless.signature_medic);
      alert(`Firma almacenada${this.paperless.signature_medic}`);
    },
  },
};
