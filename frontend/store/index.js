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
  MODAL_CHANGE_TAB,
  MODAL_RESET,
  REQUEST_NEW_INCIDENT_START,
  REQUEST_NEW_INCIDENT_SUCCESS,
  REQUEST_NEW_INCIDENT_ERROR,

} from './constants';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    error: false,
    loading: false,
    modal: { active: 'search' },
    suggestions: [],
    patient: {},
    address: {},
    emergency: {},
    post_data : {}
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
    new_incident({ commit }, term) {
      commit(REQUEST_NEW_INCIDENT_START);
      http
        .post('/emergency/new/', { params: { term } })
        .then(response => {
          commit(REQUEST_NEW_INCIDENT_SUCCESS, response.data);
        })
        .catch(err => commit(REQUEST_NEW_INCIDENT_ERROR, err));
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

    // New Incident POST emergency/new/
    [REQUEST_NEW_INCIDENT_START](state) {
      state.error = false;
      state.loading = true;
      state.post_data = state.patient + state.address
    },
    [REQUEST_NEW_INCIDENT_SUCCESS](state, data) {
      state.suggestions = data;
      state.loading = false;
    },
    [REQUEST_NEW_INCIDENT_ERROR](state, err) {
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

    // Modal
    [MODAL_CHANGE_TAB](state, data) {
      state.modal.active = data;
    },

    [MODAL_RESET](state) {
      state.suggestions = [];
      state.patient = {};
      state.address = {};
      state.emergency = {};
      state.modal.active = 'search';
    },
  },
});

export default store;
