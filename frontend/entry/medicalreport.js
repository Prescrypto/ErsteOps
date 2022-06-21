import Vue from 'vue';
import Notifications from 'vue-notification';
import VueClipboard from 'vue-clipboard2';
import VTooltip from 'v-tooltip';
import MedicalReport from 'components/MedicalReport';
// import VueSignaturePad from 'vue-signature-pad';
// import Analytics from 'components/Analytics';
import store from 'store';

Vue.use(VTooltip);
Vue.use(Notifications);
Vue.use(VueClipboard);
Vue.filter('currency', cents => cents / 100);
// Vue.use(VueSignaturePad);

// Initialize Vue component from HTML
const medicalreport = new Vue({
  el: '#medicalreport-log',
  render: h => h(MedicalReport),
  store,
});

// const analytics = new Vue({
//   el: '#analytics',
//   render: h => h(Analytics),
//   store,
// });

// const canvas = document.querySelector("canvas");

// const signaturePad = new SignaturePad(canvas);

export default { medicalreport };
