import http from 'utils/http';
import {
  REQUEST_SUGGEST_START,
  REQUEST_SUGGEST_SUCCESS,
  REQUEST_SUGGEST_ERROR,
} from 'store/constants';

export default {
  namespaced: true,
  state: {
    suggestions: [],
    error: false,
    loading: false,
  },
  actions: {
    search({ commit }, term) {
      commit(REQUEST_SUGGEST_START);
      http
        .get('/ajaxapi/getsubscriptor/', { params: { term } })
        .then(response => {
          commit(REQUEST_SUGGEST_SUCCESS, response.data);
        })
        .catch(err => commit(REQUEST_SUGGEST_ERROR, err));
    },
  },
  getters: {
    hasSuggestions(state) {
      return !!state.suggestions.length;
    },
  },
  mutations: {
    [REQUEST_SUGGEST_START](state) {
      state.error = false;
      state.loading = true;
      state.emergency = { units: [] };
    },
    [REQUEST_SUGGEST_SUCCESS](state, data) {
      state.suggestions = data;
      state.loading = false;
    },
    [REQUEST_SUGGEST_ERROR](state, err) {
      state.error = err;
      state.loading = false;
    },
  },
};
