/* eslint-disable no-param-reassign */

import Vue from 'vue';
import Vuex from 'vuex';
import http from 'utils/http';
import { REQUEST_START, REQUEST_SUCCESS, REQUEST_ERROR } from './constants';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    error: false,
    loading: false,
    suggestions: [],
  },

  actions: {
    search({ commit }, term) {
      commit(REQUEST_START);
      http
        .get('getsubscriptor/', {
          params: { term },
        })
        .then(response => {
          commit(REQUEST_SUCCESS, response.data);
        })
        .catch(err => {
          commit(REQUEST_ERROR, err);
        });
    },
  },

  getters: {
    hasSuggestions: state => !!state.suggestions.length,
  },

  mutations: {
    [REQUEST_START](state) {
      state.error = false;
      state.loading = true;
    },
    [REQUEST_SUCCESS](state, data) {
      state.suggestions = data;
      state.loading = false;
    },
    [REQUEST_ERROR](state, err) {
      state.error = err;
      state.loading = false;
    },
  },
});

export default store;
