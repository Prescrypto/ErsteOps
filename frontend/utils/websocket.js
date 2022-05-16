/* eslint-disable no-param-reassign */

import { findIndex } from 'lodash/fp';
import {
  EMERGENCIES_ADD,
  EMERGENCIES_UPDATE,
  // EMERGENCIES_REMOVE,
} from 'store/constants';

export default function createWebSocketPlugin(socket) {
  return ({ commit, state }) => {
    // Add to emergencies when receiving new data
    socket.onmessage = message => {
      const dataTemp = JSON.parse(message.data);
      const data = dataTemp;
      const { id } = data;
      const { emergencies } = state;

      // If index is not found, add new emergency
      // If index is found, update existing emergency
      const index = findIndex(emergency => emergency.id === id)(emergencies);
      if (index < 0) {
        commit(EMERGENCIES_ADD, data);
      } else {
        commit(EMERGENCIES_UPDATE, { index, data });
      }
    };
  };
}
