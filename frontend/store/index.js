/* eslint-disable no-param-reassign */

import Vue from 'vue';
import Vuex from 'vuex';
import {
  map,
  sortBy,
  flow,
  reverse,
  filter,
  findIndex,
  uniq,
  uniqBy,
  includes,
} from 'lodash/fp';
import http from 'utils/http';
import { removePrefix } from 'utils/normalize';
import { emergencies, units } from 'utils/preload';
import { ws } from 'utils/url';
import createWebSocketPlugin from 'utils/websocket';
import ReconnectingWebSocket from 'reconnecting-websocket';
import {
  REQUEST_SUGGEST_START,
  REQUEST_SUGGEST_SUCCESS,
  REQUEST_SUGGEST_ERROR,
  REQUEST_PATIENT_START,
  REQUEST_PATIENT_SUCCESS,
  REQUEST_PATIENT_ERROR,
  REQUEST_UNITS_START,
  REQUEST_UNITS_SUCCESS,
  REQUEST_UNITS_ERROR,
  REQUEST_EMERGENCY_START,
  REQUEST_EMERGENCY_SUCCESS,
  REQUEST_EMERGENCY_ERROR,
  REQUEST_EMERGENCY_TEXT_START,
  REQUEST_EMERGENCY_TEXT_SUCCESS,
  REQUEST_EMERGENCY_TEXT_ERROR,
  EMERGENCY_TEXT_CLEAR,
  SELECT_ADDRESS,
  MODAL_CHANGE_TAB,
  MODAL_RESET,
  MODAL_UNITS_ADD,
  MODAL_UNITS_REMOVE,
  MODAL_UNITS_SET,
  REQUEST_NEW_INCIDENT_START,
  REQUEST_NEW_INCIDENT_SUCCESS,
  REQUEST_NEW_INCIDENT_ERROR,
  EMERGENCIES_ADD,
  EMERGENCIES_UPDATE,
  EMERGENCY_SET_INACTIVE_START,
  EMERGENCY_SET_INACTIVE_SUCCESS,
  EMERGENCY_SET_INACTIVE_ERROR,
  EMERGENCY_TOGGLE_ACTIVE,
} from './constants';

// Use VueX
Vue.use(Vuex);

// Create VueX store
const store = new Vuex.Store({
  state: {
    error: false,
    loading: false,
    modal: {
      active: 'search',
      address: {},
    },
    units,
    selected: [],
    suggestions: [],
    emergencies,
    emergency: {
      is_active: true,
      units: [],
    },
    emergencyText: '',
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
    newIncident({ commit }, data) {
      commit(REQUEST_NEW_INCIDENT_START);
      return http
        .post(`/emergency/new/${data.id || ''}`, data)
        .then(response => {
          commit(REQUEST_NEW_INCIDENT_SUCCESS, response.data);
        })
        .catch(err => {
          commit(REQUEST_NEW_INCIDENT_ERROR, err);
          throw err;
        });
    },
    patient({ commit }, target) {
      commit(REQUEST_PATIENT_START);
      http
        .get(`/emergency/ajax/patient/${target}/`)
        .then(response => {
          const { data } = response;
          const addresses = JSON.parse(data.addresses).map(address =>
            removePrefix(address, /id_/)
          );
          const normalized = removePrefix({ ...data, addresses }, /id_/);
          commit(REQUEST_PATIENT_SUCCESS, normalized);
        })
        .catch(err => commit(REQUEST_PATIENT_ERROR, err));
    },
    units({ commit }) {
      commit(REQUEST_UNITS_START);
      http
        .get('/units/ajax/local/')
        .then(response => {
          const { data } = response;
          const flatUnits = map(u => ({ id: u.pk, ...u.fields }))(data);
          commit(REQUEST_UNITS_SUCCESS, flatUnits);
        })
        .catch(err => commit(REQUEST_UNITS_ERROR, err));
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
    emergencyDetails({ commit }, id) {
      commit(REQUEST_EMERGENCY_TEXT_START);
      return http
        .get(`/emergency/detail_text/${id}/`)
        .then(response => commit(REQUEST_EMERGENCY_TEXT_SUCCESS, response.data))
        .catch(err => {
          commit(REQUEST_EMERGENCY_TEXT_ERROR, err);
          throw err;
        });
    },
    stopTimer({ commit }, id) {
      commit(EMERGENCY_SET_INACTIVE_START);
      http
        .get(`/emergency/ajax/end/${id}/`)
        .then(() => commit(EMERGENCY_SET_INACTIVE_SUCCESS, id))
        .catch(err => commit(EMERGENCY_SET_INACTIVE_ERROR, err));
    },
  },

  getters: {
    hasSuggestions: state => !!state.suggestions.length,

    // units
    activeUnits: state => filter(unit => unit.is_active)(state.units),
    activeUnitsCount: (state, getters) => getters.activeUnits.length,
    selectedUnits: state => state.selected,
    combinedUnits: (state, getters) =>
      uniq([
        ...filter(unit => includes(unit.id)(state.emergency.units))(
          state.units
        ),
        ...getters.selectedUnits,
      ]),

    // emergencies
    activeEmergencies: state =>
      filter(emergency => emergency.is_active)(state.emergencies),
    sortActiveEmergencies: (state, getters) =>
      flow(
        sortBy(emergency => new Date(emergency.start_time).getTime()),
        reverse
      )(getters.activeEmergencies),
    activeEmergencyCount: (state, getters) => getters.activeEmergencies.length,
  },

  mutations: {
    // Suggestions
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

    // New Incident
    [REQUEST_NEW_INCIDENT_START](state) {
      state.error = false;
      state.loading = true;
    },
    [REQUEST_NEW_INCIDENT_SUCCESS](state) {
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
      state.modal.address = {};
    },
    [REQUEST_PATIENT_SUCCESS](state, data) {
      state.emergency = data;
      state.loading = false;
    },
    [REQUEST_PATIENT_ERROR](state, err) {
      state.error = err;
      state.loading = false;
    },

    // Units
    [REQUEST_UNITS_START](state) {
      state.error = false;
      state.loading = true;
    },
    [REQUEST_UNITS_SUCCESS](state, data) {
      state.units = data;
      state.loading = false;
    },
    [REQUEST_UNITS_ERROR](state, err) {
      state.error = err;
      state.loading = false;
    },

    // Emergency
    [REQUEST_EMERGENCY_START](state) {
      state.error = false;
      state.loading = true;
    },
    [REQUEST_EMERGENCY_SUCCESS](state, data) {
      state.emergency = data;
      state.loading = false;
    },
    [REQUEST_EMERGENCY_ERROR](state, err) {
      state.error = err;
      state.loading = false;
    },

    // Emergency Text
    [REQUEST_EMERGENCY_TEXT_START](state) {
      state.error = false;
      state.loading = true;
    },
    [REQUEST_EMERGENCY_TEXT_SUCCESS](state, data) {
      state.emergencyText = data;
      state.loading = false;
    },
    [REQUEST_EMERGENCY_TEXT_ERROR](state, err) {
      state.error = err;
      state.loading = false;
    },
    [EMERGENCY_TEXT_CLEAR](state) {
      state.error = false;
      state.emergencyText = '';
    },

    // Select patient address
    [SELECT_ADDRESS](state, data) {
      state.modal.address = data;
    },

    // Modal
    [MODAL_CHANGE_TAB](state, data) {
      state.modal.active = data;
    },

    [MODAL_RESET](state) {
      state.suggestions = [];
      state.modal.address = {};
      state.selected = [];
      state.emergency = { units: [] };
      state.modal.active = 'search';
    },

    [MODAL_UNITS_ADD](state, unit) {
      state.selected.push(unit);
      state.selected = uniqBy('id')(state.selected);

      Vue.set(
        state.emergency,
        'units',
        uniq([...state.emergency.units, ...map(u => u.id)(state.selected)])
      );
    },

    [MODAL_UNITS_REMOVE](state, unit) {
      state.selected = filter(u => unit.id !== u.id)(state.selected);

      Vue.set(
        state.emergency,
        'units',
        filter(u => unit.id !== u)(state.emergency.units)
      );
    },

    [MODAL_UNITS_SET](state, all) {
      state.selected = all;
      Vue.set(state.emergencies, 'units', all);
    },

    // Emergency i.e. modal data
    [EMERGENCY_TOGGLE_ACTIVE](state) {
      state.emergency.is_active = !state.emergency.is_active;
    },

    // Emergencies i.e. dashboard log data
    [EMERGENCIES_ADD](state, data) {
      state.emergencies.push(data);
    },
    [EMERGENCIES_UPDATE](state, { index, data }) {
      Vue.set(state.emergencies, index, data);
    },
    [EMERGENCY_SET_INACTIVE_START](state) {
      state.error = false;
      state.loading = true;
    },
    [EMERGENCY_SET_INACTIVE_SUCCESS](state, id) {
      const index = findIndex(e => e.id === id)(state.emergencies);
      Vue.set(state.emergencies, index, {
        ...state.emergencies[index],
        is_active: false,
      });
      state.loading = false;
    },
    [EMERGENCY_SET_INACTIVE_ERROR](state, err) {
      state.error = err;
      state.loading = false;
    },
  },

  plugins: [
    createWebSocketPlugin(new ReconnectingWebSocket(`${ws}/notify/emergency/`)),
  ],
});

export default store;
