/* eslint-disable import/prefer-default-export */

export function removePrefix(obj, regex) {
  const copy = {};

  Object.keys(obj).forEach(key => {
    copy[key.replace(regex, '')] = obj[key];
  });

  return copy;
}
