import { mapState } from 'vuex';
import Loader from 'vue-spinner/src/ScaleLoader.vue';

export default {
  name: 'emergency-derivation',
  props: ['emergency'],

  data: () => ({
    // hospitals: [],
    // enableRadio: false,
    selected: null,
    message: null,
    reception: null,
  }),

  components: { Loader },
  mounted() {
    // this.getHospitals();
  },
  computed: {
    // mapHospitas is defined in /utils/preload.js
    ...mapState(['loading', 'emergency', 'mapHospitals']),
    isValid() {
      return this.selected != null;
    },

    emergency_link() {
      const eName = `/admin/emergency/emergency/${this.emergency.id}/change/#/tab/module_5/`;
      return eName;
    },
  },
  methods: {
    async submit(e) {
      try {
        e.stopPropagation();
        e.preventDefault();

        // const response = await this.setUpdateTimer({
        //   id: this.emergency.id,
        //   timer_type: this.timerPicked,
        // });

        // this.$emit('updatetimer', response);

        this.$notify({
          text: `Se agrego la derivacion al del auxilio existosamente ${this.emergency.id}`,
          type: 'success',
        });
      } catch (err) {
        this.$emit('error', err);
        this.$notify({
          text: `No se pudo actualizar derivacion del auxilio${err}`,
          type: 'error',
        });
      }
    },
  },
};
