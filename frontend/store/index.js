/* eslint-disable no-param-reassign */

import Vue from 'vue';
import Vuex from 'vuex';
import http from 'utils/http';
import {
  REQUEST_SUGGEST_START,
  REQUEST_SUGGEST_SUCCESS,
  REQUEST_SUGGEST_ERROR,
  REQUEST_PATIENT_START,
  REQUEST_PATIENT_SUCCESS,
  REQUEST_PATIENT_ERROR,
} from './constants';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    error: false,
    loading: false,
    suggestions: [],
  },

  actions: {
    search({ commit }, term) {
      commit(REQUEST_SUGGEST_START);
      http
        .get('/ajaxapi/getsubscriptor/', {
          params: { term },
        })
        .then(response => {
          commit(REQUEST_SUGGEST_SUCCESS, response.data);
        })
        .catch(err => {
          commit(REQUEST_SUGGEST_ERROR, err);
        });
    },
    patient({ commit }, target) {
      commit(REQUEST_PATIENT_START);
      http
        .get(`/emergency/ajax/patient/${target}/`)
        .then(response => {
          const { data } = response;
          const addresses = JSON.parse(data.addresses);
          commit(REQUEST_PATIENT_SUCCESS, { ...data, addresses });
        })
        .catch(err => {
          commit(REQUEST_PATIENT_ERROR, err);
        });
    },
  },

  getters: {
    hasSuggestions: state => !!state.suggestions.length,
  },

  mutations: {
    // Suggestions
    [REQUEST_SUGGEST_START](state) {
      state.error = false;
      state.loading = true;
    },
    [REQUEST_SUGGEST_SUCCESS](state, data) {
      state.suggestions = data;
      state.loading = false;
    },
    [REQUEST_SUGGEST_ERROR](state, err) {
      state.error = err;
      state.loading = false;
    },

    // Patients
    [REQUEST_PATIENT_START](state) {
      state.error = false;
      state.loading = true;
    },
    [REQUEST_PATIENT_SUCCESS](state, data) {
      state.patient = data;
      state.loading = false;
    },
    [REQUEST_PATIENT_ERROR](state, err) {
      state.error = err;
      state.loading = false;
    },
  },
});

export default store;
