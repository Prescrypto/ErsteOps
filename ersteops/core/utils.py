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
        self.auth = HTTPBasicAuth(settings.ODOO_USERNAME, settings.ODOO_PASSWORD)
        self.url = 'https://' + settings.ODOO_URL + '/api/auth/get_tokens'
        self.headers = {"Content-Type": 'content-type: text/html; chartset=UTF-8'}
        print ("******** init *******")
        print (str(self))
        #self.admin_user = admin_user

    def get_token(self):
        url = self.url #+ '/api/auth/get_tokens'

        response = requests.post(url, auth=self.auth)
        return response.json()

