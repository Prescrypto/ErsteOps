import { mapState, mapActions, mapGetters, mapMutations } from 'vuex';
import Loader from 'vue-spinner/src/ScaleLoader.vue';
import { MODAL_CHANGE_TAB } from 'store/constants';

export default {
  name: 'search',

  components: { Loader },

  data() {
    // query is for the input
    // pristine indicates there's no prior search
    return {
      query: '',
      pristine: true,
    };
  },

  computed: {
    invalid() {
      return (((this.fields || {}).$search || {}).term || {}).invalid;
    },
    ...mapState(['loading', 'suggestions']),
    ...mapGetters(['hasSuggestions']),
  },

  methods: {
    // on submit, disable the default <form> submit, indicate the form is
    // dirty, and run the search action with the input value
    submit(scope) {
      this.$validator.validateAll(scope).then(valid => {
        if (valid) {
          this.pristine = false;
          this.search(this.query);
        }
      });
    },

    populate(target) {
      this.patient(target);
      this.changeTab('patient');
      window.$(`#nav-patient-tab`).tab('show');
    },
    ...mapMutations({
      changeTab: MODAL_CHANGE_TAB,
    }),
    ...mapActions(['search', 'patient']),
  },
};
