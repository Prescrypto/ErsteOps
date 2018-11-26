// import { mapActions } from 'vuex';

export default {
  name: 'dashboard-timers',
  props: ['emergency'],
  data: () => ({
    timerPicked: null,
    // isOpen: true,
  }),
  // $_veeValidate: {
  //  validator: 'new',

  // },
  computed: {
    isValid() {
      return this.timerPicked != null;
    },
  },
  methods: {
    show_timers() {
      return true;
    },
    async submit(e) {
      try {
        e.stopPropagation();
        e.preventDefault();
        // const response = await this.setFinalGrade({
        //   id: this.emergency.id,
        //   attention_final_grade: this.finalGrade.name,
        //   attention_justification: this.justification,
        // });
        this.$emit('graded', '200');

        this.$notify({
          text: `Se actualizo el timer del auxilio existosamente ${
            this.emergency.id
          }`,
          type: 'success',
        });
        // this.popover.$emit('apply-hide');
        // this.popover.$emit('close-directive');
        // e.$emit('apply-hide');
        // this.stoppedTimer=false;
        // this.popover.$emit('hide');
        // console.log(this);
      } catch (err) {
        this.$emit('error', err);
        this.$notify({
          text: 'No se pudo actualizar el timer del auxilio',
          type: 'error',
        });
      }
    },
  },
};
