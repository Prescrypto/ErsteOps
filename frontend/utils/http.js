import { url } from 'utils/url';
import axios from 'axios';
import cookie from 'js-cookie';

export default axios.create({
  baseURL: `${url}`,
  headers: {
    'X-Requested-With': 'XMLHttpRequest',
    'X-CSRFToken': cookie.get('csrftoken'),
  },
});
