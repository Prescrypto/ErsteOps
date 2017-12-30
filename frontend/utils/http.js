import { url } from 'utils/url';
import axios from 'axios';

export default axios.create({
  baseURL: `${url}/ajaxapi/`,
  headers: {
    'X-Requested-With': 'XMLHttpRequest',
  },
});
