import { isProd } from './env';

const { host } = window.location;

export const ws = isProd ? `wss://${host}` : `ws://${host}`;
export const url = '';
