import 'filters/time-since';
import AirWay from 'components/AirWay';
import PhysicalExploration from 'components/PhysicalExploration';
import SignatureClient from 'components/SignatureClient';
import Medications from 'components/Medications';
import { mapActions } from 'vuex';
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
    eye_options: [
      { text: 'Isocoria', value: 'Isocoria' },
      { text: 'Midriasis', value: 'Midriasis' },
      { text: 'Miosis', value: 'Miosis' },
      { text: 'Anisocoria', value: 'Anisocoria' },
    ],
    // const canvas = document.querySelector("canvas");
    // const signaturePad = new SignaturePad(canvas);
  }),
  components: { AirWay, PhysicalExploration, SignatureClient, Medications },
  methods: {
    ...mapActions('newMedicalReport', ['createMedicalReport']),

    async submit(e) {
      // e.preventDefault();
      // this.$validator
      //   .validateAll('paperless')
      //   .then(valid => {
      //     if (valid) {
      //       return this.setNewMedicalReport(this.form);
      //     }
      //     throw new Error();
      //   })
      //   .then(() => {
      //     this.$notify({
      //       text: 'Se ha guardado el parte medico en el sistema.',
      //       type: 'success',
      //     });
      //     // close modal after submit if no errors
      //     // this.$modal.hide('incident-modal');
      //   })
      //   .catch(() => {
      //     this.$notify({
      //       text: 'Hubo un error al guardar el parte medico, intente de nuevo.',
      //       type: 'error',
      //     });
      //   });
      try {
        e.stopPropagation();
        e.preventDefault();
        // var form = $(this);
        // var jsonForm= form.serialize();
        // var jsonForm=this.$refs.form.serialize();
        const jsonForm = JSON.stringify(this.paperless);
        console.log('SUBMIT');
        console.log(jsonForm);

        const response = await this.createMedicalReport({
          // id: this.emergency.id,
          // id: this.paperless.service_code,
          // fe_paperless: this.paperless,
          // paperless,
          paperless: jsonForm,
          // timer_type: this.timerPicked,
        });
        this.$emit('newmedicalreport', response);

        this.$notify({
          text: `Se creo el parte medico existosamente: ${
            // this.emergency.id
            this.paperless.service_code
          }`,
          type: 'success',
        });
      } catch (err) {
        this.$emit('error', err);
        this.$notify({
          text: `No se pudo crear el parte medico - ${err}`,
          type: 'error',
        });
      }
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
