import Vue from 'vue';
import Notifications from 'vue-notification';
import VueClipboard from 'vue-clipboard2';
import VTooltip from 'v-tooltip';
import MedicalReport from 'components/MedicalReport';
import Geoposition from 'components/Geoposition';
import VeeValidate, { Validator } from 'vee-validate';
import es from 'vee-validate/dist/locale/es';
import * as VueGoogleMaps from 'vue2-google-maps';
import VueSignaturePad from 'vue-signature-pad';
// import VueSignature from "vue-signature-pad";
// import Analytics from 'components/Analytics';
import store from 'store';

// const paperless = window.erste.paperless;

Vue.use(VTooltip);
Vue.use(Notifications);
Vue.use(VueClipboard);
Vue.filter('currency', cents => cents / 100);
Vue.use(VeeValidate, { inject: false });
Validator.localize('es', es);
Vue.use(VueGoogleMaps, {
  load: {
    key: window.erste.paperless.geo_key,
    libraries: 'places',
  },
});
Vue.use(VueSignaturePad);
// Vue.use(VueSignature);
// Vue.use(VueSignature);

// Initialize Vue component from HTML
const medicalreport = new Vue({
  el: '#medicalreport-log',
  render: h => h(MedicalReport),
  store,
});

const geoposition = new Vue({
  el: '#geoposition-map',
  render: h => h(Geoposition),
  store,
});

// const canvas = this.$refs.signaturePadCanvas;
// const signaturePad = new SignaturePad(canvas);

// const signatureclient = new Vue ({
//   el: '#signature-client',
//   render: h => h(VueSignaturePad),
//   store,
// });
// const

// const analytics = new Vue({
//   el: '#analytics',
//   render: h => h(Analytics),
//   store,
// });

// const canvas = document.querySelector("canvas");

// const signaturePad = new SignaturePad(canvas);

export default { medicalreport, geoposition };
