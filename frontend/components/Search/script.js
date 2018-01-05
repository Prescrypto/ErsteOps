import { mapState, mapActions, mapGetters } from 'vuex';
import Loader from 'vue-spinner/src/ScaleLoader.vue';

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
      return this.fields.term.invalid;
    },

    // loading is for hiding the spinner
    // suggestions is the server results array
    ...mapState({
      loading: 'loading',
      suggestions: 'suggestions',
    }),
    // memoized computed property that indicates whether there are suggestions
    ...mapGetters(['hasSuggestions']),
  },

  methods: {
    // on submit, disable the default <form> submit, indicate the form is
    // dirty, and run the search action with the input value
    submit() {
      this.$validator.validateAll().then(valid => {
        if (valid) {
          this.pristine = false;
          this.search(this.query);
        }
      });
    },

    populate(target) {
      this.patient(target);
      window.$(`#nav-patient-tab`).tab('show');
    },

    // maps the search action from the store to the component
    ...mapActions(['search', 'patient']),
  },
};
