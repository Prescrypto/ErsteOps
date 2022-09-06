/* eslint-disable import/prefer-default-export */

import map from 'lodash/fp/map';
import reduce from 'lodash/fp/reduce';

// Initialize empty data store
const { incidents, units: onLoadUnits, hospitals } = window.erste;

// Flatten emergencies
export const emergencies =
  map(emergency => ({ id: emergency.pk, ...emergency.fields }))(incidents) ||
  [];

// Flatten units
export const units = reduce((collection, unit) => {
  collection[unit.pk] = { id: unit.pk, ...unit.fields };
  return collection;
}, {})(onLoadUnits);

// Map hospitals to clean json data extras import using ...mapState
export const mapHospitals =
  map(attentionHospital => ({
    id: attentionHospital.pk,
    ...attentionHospital.fields,
  }))(hospitals) || [];

// export const paperlessData =
//   map(paperless => ({ geo_key: paperless.geo_key, ...paperless.fields }))(paperless) ||[];
