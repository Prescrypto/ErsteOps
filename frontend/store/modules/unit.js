import reduce from 'lodash/fp/reduce';
import { units } from 'utils/preload';
import http from 'utils/http';
import {
  UNIT_DETAILS_START,
  UNIT_DETAILS_SUCCESS,
  UNIT_DETAILS_ERROR,
} from 'store/constants';

const createCollection = data =>
  reduce((collection, unit) => {
    collection[unit.pk] = { id: unit.pk, ...unit.fields };
    return collection;
  }, {})(data);

export default {
  namespaced: true,
  state: { units },
  actions: {
    details({ commit }, id) {
      commit(UNIT_DETAILS_START);
      return http
        .get(`/units/ajax/detail/${id}`)
        .then(response => commit(UNIT_DETAILS_SUCCESS, response.data))
        .catch(err => {
          commit(UNIT_DETAILS_ERROR, err);
          throw err;
        });
    },
  },
  mutations: {
    [UNIT_DETAILS_START](state) {
      state.error = false;
      state.loading = true;
    },
    [UNIT_DETAILS_SUCCESS](state, data) {
      state.loading = false;
      state.units = { ...state.units, ...createCollection(data) };
    },
    [UNIT_DETAILS_ERROR](state, err) {
      state.error = err;
      state.loading = false;
    },
  },
};
