import 'filters/time-since';
import AirWay from 'components/AirWay';
import PhysicalExploration from 'components/PhysicalExploration';
import SignatureClient from 'components/SignatureClient';
import Medications from 'components/Medications';
// import GoogleMap from './components/GoogleMap.vue'
// import find from 'lodash/fp/find';
// import { mapState, mapActions, mapMutations, mapGetters } from 'vuex';

export default {
  name: 'medicalreport-log',
  inject: ['$validator'],
  data: () => ({
    gender: '',
    attention_place: '',
    service_kind: '',
    consultation_motive: [],
    traumatics: '',
    traumatics_type: [],
    airway: [],
    patological_background: [],
    normal_elements: [],
    inmovilization: [],
    fe_inmovilization: false,
    derivarion: false,
    derivation_type: '',
    state_of_health: '',
    loading: false,
    paperless: window.erste.paperless,
    // paperless_dict: window.erste.paperles_dict,
    unknow_patient: false,
    electrocardiogram: false,
    hemoderivado: false,
    cardiovascular: false,
    farmacologico: false,
    demarcation: false,
    // const canvas = document.querySelector("canvas");
    // const signaturePad = new SignaturePad(canvas);
  }),
  components: { AirWay, PhysicalExploration, SignatureClient, Medications },
  methods: {
    submit(e) {
      e.preventDefault();
      this.$validator
        .validateAll('emergency')
        .then(valid => {
          if (valid) {
            return this.newMedicalReport(this.form);
          }
          throw new Error();
        })
        .then(() => {
          this.$notify({
            text: 'Se ha guardado el parte medico en el sistema.',
            type: 'success',
          });
          // close modal after submit if no errors
          // this.$modal.hide('incident-modal');
        })
        .catch(() => {
          this.$notify({
            text: 'Hubo un error al guardar el parte medico, intente de nuevo.',
            type: 'error',
          });
        });
    },
  },
  $_veeValidate: {
    validator: 'new',
  },
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
