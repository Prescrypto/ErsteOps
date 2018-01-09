import { isProd } from './env';

const { host, protocol } = window.erste.url;

export const ws = isProd ? `wss://${host}` : `ws://${host}`;
export const url = `${protocol}://${host}`;
