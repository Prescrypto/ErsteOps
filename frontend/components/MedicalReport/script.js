import 'filters/time-since';
// import find from 'lodash/fp/find';
// import { mapState, mapActions, mapMutations, mapGetters } from 'vuex';

export default {
  name: 'medicalreport-log',
  data: () => ({
    gender: '',
    attention_place: '',
    service_kind: '',
    consultation_motive: '',
    traumatics: '',
    traumatics_type: '',
    airway: '',
    patological_background: '',
    normal_elements: '',
    derivation: '',
    state_of_health: '',
    // const canvas = document.querySelector("canvas");
    // const signaturePad = new SignaturePad(canvas);
  }),
  // components: {signaturePad} ,
  // methods: {
  //   undo() {
  //     this.$refs.signaturePad.undoSignature();
  //   },
  //   save() {
  //     const { isEmpty, data } = this.$refs.signaturePad.saveSignature();
  //     console.log(isEmpty);
  //     console.log(data);
  //   }
  // }
};
