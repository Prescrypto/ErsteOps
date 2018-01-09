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
  REQUEST_EMERGENCY_START,
  REQUEST_EMERGENCY_SUCCESS,
  REQUEST_EMERGENCY_ERROR,
  SELECT_ADDRESS,
} from './constants';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    error: false,
    loading: false,
    suggestions: [],
    patient: {},
    address: {},
    emergency: {},
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
    patient({ commit }, target) {
      commit(REQUEST_PATIENT_START);
      http
        .get(`/emergency/ajax/patient/${target}/`)
        .then(response => {
          const { data } = response;
          const addresses = JSON.parse(data.addresses);
          commit(REQUEST_PATIENT_SUCCESS, { ...data, addresses });
        })
        .catch(err => commit(REQUEST_PATIENT_ERROR, err));
    },
    emergency({ commit }, id) {
      commit(REQUEST_EMERGENCY_START);
      http
        .get(`/emergency/ajax/detail/${id}/`)
        .then(response => {
          const emergency = response.data[0];
          commit(REQUEST_EMERGENCY_SUCCESS, {
            id: emergency.pk,
            ...emergency.fields,
          });
        })
        .catch(err => commit(REQUEST_EMERGENCY_ERROR, err));
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
      state.patient = {};
      state.address = {};
    },
    [REQUEST_SUGGEST_SUCCESS](state, data) {
      state.suggestions = data;
      state.loading = false;
    },
    [REQUEST_SUGGEST_ERROR](state, err) {
      state.error = err;
      state.loading = false;
    },

    // Patient
    [REQUEST_PATIENT_START](state) {
      state.error = false;
      state.loading = true;
      state.patient = {};
      state.address = {};
    },
    [REQUEST_PATIENT_SUCCESS](state, data) {
      state.patient = data;
      state.loading = false;
    },
    [REQUEST_PATIENT_ERROR](state, err) {
      state.error = err;
      state.loading = false;
    },

    // Emergency
    [REQUEST_EMERGENCY_START](state) {
      state.error = false;
      state.loading = true;
    },
    [REQUEST_EMERGENCY_SUCCESS](state, data) {
      // eslint-disable-line jshint ignore:line
      state.emergency = data;
      state.loading = false;
    },
    [REQUEST_EMERGENCY_ERROR](state, err) {
      state.error = err;
      state.loading = false;
    },

    // Select patient address
    [SELECT_ADDRESS](state, data) {
      state.address = data;
    },
  },
});

export default store;
