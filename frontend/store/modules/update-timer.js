import http from 'utils/http';
import {
  EMERGENCY_SET_TIMER_UPDATE_START,
  EMERGENCY_SET_TIMER_UPDATE_SUCCESS,
  EMERGENCY_SET_TIMER_UPDATE_ERROR,
} from 'store/constants';

export default {
  namespaced: true,
  state: {
    error: false,
    loading: false,
  },
  actions: {
    setUpdateTimer({ commit }, data) {
      console.log('setupdatetomer!');
      commit(EMERGENCY_SET_TIMER_UPDATE_START);
      return http
        .post('/emergency/ajax/update_timer/', data)
        .then(response => {
          commit(EMERGENCY_SET_TIMER_UPDATE_SUCCESS, response.data);
        })
        .catch(err => {
          commit(EMERGENCY_SET_TIMER_UPDATE_ERROR, err);
          throw err;
        });
    },
  },
  mutations: {
    [EMERGENCY_SET_TIMER_UPDATE_START](state) {
      state.error = false;
      state.loading = true;
    },
    [EMERGENCY_SET_TIMER_UPDATE_SUCCESS](state) {
      state.loading = false;
    },
    [EMERGENCY_SET_TIMER_UPDATE_ERROR](state, err) {
      state.error = err;
      state.loading = false;
    },
  },
};
