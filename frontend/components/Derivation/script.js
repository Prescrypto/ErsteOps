import { mapState } from 'vuex';
import Loader from 'vue-spinner/src/ScaleLoader.vue';

export default {
  name: 'emergency-derivation',
  props: ['emergency'],

  data: () => ({
    // hospitals: [],
    // enableRadio: false,
  }),

  components: { Loader },
  mounted() {
    // this.getHospitals();
  },
  computed: {
    // mapHospitas is defined in /utils/preload.js
    ...mapState(['loading', 'emergency', 'mapHospitals']),

    emergency_link() {
      const eName = `/admin/emergency/emergency/${this.emergency.id}/change/#/tab/module_5/`;
      return eName;
    },
  },
  methods: {},
};
