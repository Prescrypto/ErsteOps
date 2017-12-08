# -*- encoding: utf-8 -*-
import json
import base64
import logging
import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings

# Calculate event duration
def eventDuration(start_duration,end_duration):
    return end_duration - start_duration

class OdooApi(object):

    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger('django_info')
        #self.auth = HTTPBasicAuth(settings.ODOO_USERNAME, settings.ODOO_PASSWORD)
        self.url = settings.BASE_URL + settings.ODOO_URL
        self.headers = {"Content-Type": "text/html"}


    def get_token(self):
        url = self.url + '/api/auth/get_tokens'
        payload = {'username': settings.ODOO_USERNAME, 'password': settings.ODOO_PASSWORD}
        response = requests.post(url, data=json.dumps(payload), headers=self.headers)

        return response.json()


