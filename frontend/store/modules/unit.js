import reduce from 'lodash/fp/reduce';
import http from 'utils/http';
import {
  UNIT_DETAILS_START,
  UNIT_DETAILS_SUCCESS,
  UNIT_DETAILS_ERROR,
} from 'store/constants';

export default {
  namespaced: true,
  state: {
    unit: {},
  },
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
      state.unit = reduce((collection, unit) => {
        collection[unit.pk] = { ...unit.pk, ...unit.fields };
        return collection;
      }, {})(data);
    },
    [UNIT_DETAILS_ERROR](state, err) {
      state.error = err;
      state.loading = false;
    },
  },
};
