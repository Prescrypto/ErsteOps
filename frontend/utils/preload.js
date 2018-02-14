/* eslint-disable import/prefer-default-export */

import { map } from 'lodash/fp';

// Initialize empty data store
const { incidents, units: onLoadUnits } = window.erste;

// Flatten emergencies
export const emergencies =
  map(emergency => ({ id: emergency.pk, ...emergency.fields }))(incidents) ||
  [];

// Flatten units
export const units =
  map(unit => ({ id: unit.pk, ...unit.fields }))(onLoadUnits) || [];
