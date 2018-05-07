import http from 'utils/http';
import {
  EMERGENCY_SET_FINAL_GRADE_START,
  EMERGENCY_SET_FINAL_GRADE_SUCCESS,
  EMERGENCY_SET_FINAL_GRADE_ERROR,
} from 'store/constants';

export default {
  namespaced: true,
  state: {
    error: false,
    loading: false,
  },
  actions: {
    setFinalGrade({ commit }, data) {
      commit(EMERGENCY_SET_FINAL_GRADE_START);
      return http
        .post('/emergency/ajax/change_grade/', data)
        .then(response => {
          commit(EMERGENCY_SET_FINAL_GRADE_SUCCESS, response.data);
        })
        .catch(err => {
          commit(EMERGENCY_SET_FINAL_GRADE_ERROR, err);
          throw err;
        });
    },
  },
  mutations: {
    [EMERGENCY_SET_FINAL_GRADE_START](state) {
      state.error = false;
      state.loading = true;
    },
    [EMERGENCY_SET_FINAL_GRADE_SUCCESS](state) {
      state.loading = false;
    },
    [EMERGENCY_SET_FINAL_GRADE_ERROR](state, err) {
      state.error = err;
      state.loading = false;
    },
  },
};
