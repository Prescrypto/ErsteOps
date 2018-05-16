/* eslint-disable import/prefer-default-export */

import map from 'lodash/fp/map';
import reduce from 'lodash/fp/reduce';

// Initialize empty data store
const { incidents, units: onLoadUnits } = window.erste;

// Flatten emergencies
export const emergencies =
  map(emergency => ({ id: emergency.pk, ...emergency.fields }))(incidents) ||
  [];

// Flatten units
export const units = reduce((collection, unit) => {
  collection[unit.pk] = { id: unit.pk, ...unit.fields };
  return collection;
}, {})(onLoadUnits);
