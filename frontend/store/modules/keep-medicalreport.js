import http from 'utils/http';
import {
  REQUEST_MEDICALREPORT_START,
  REQUEST_MEDICALREPORT_SUCCESS,
  REQUEST_MEDICALREPORT_ERROR,
} from 'store/constants';

export default {
  namespaced: true,
  state: {
    error: false,
    loading: false,
  },
  actions: {
    createMedicalReport({ commit }, data) {
      // console.log('setupdatetomer!');
      commit(REQUEST_MEDICALREPORT_START);
      return (
        http
          // .post('/emergency/ajax/update_timer/', data)
          // .post(`/paperless/ajax/new/${data.id || ''}/`, data)
          .post(`/paperless/ajax/new/`, data)
          .then(response => {
            commit(REQUEST_MEDICALREPORT_SUCCESS, response.data);
            window.location = '/paperless/';
          })
          .catch(err => {
            commit(REQUEST_MEDICALREPORT_ERROR, err);
            throw err;
          })
      );
    },
  },
  mutations: {
    [REQUEST_MEDICALREPORT_START](state) {
      state.error = false;
      state.loading = true;
    },
    [REQUEST_MEDICALREPORT_SUCCESS](state) {
      state.loading = false;
    },
    [REQUEST_MEDICALREPORT_ERROR](state, err) {
      state.error = err;
      state.loading = false;
    },
  },
};

// newMedicalReport({ commit }, data) {
//   commit(REQUEST_MEDICALREPORT_START);
//   return http
//     .post(`/paperless/new/${data.id || ''}`, data)
//     .then(response => {
//       commit(REQUEST_MEDICALREPORT_SUCCESS, response.data);
//     })
//     .catch(err => {
//       commit(REQUEST_MEDICALREPORT_ERROR, err);
//       throw err;
//     });
// },
