/* eslint-disable import/prefer-default-export */

import { map } from 'lodash/fp';

// Initialize empty data store
const { incidents } = window.erste;

// Add emergencies and sort by start time
export const emergencies =
  map(emergency => ({ id: emergency.pk, ...emergency.fields }))(incidents) ||
  [];
