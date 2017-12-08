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
        self.url = 'https://' + settings.ODOO_URL #+ '/api/auth/get_tokens'
        self.headers = {"Content-Type": 'text/html'}
        #print ("******** init *******")
        #print (str(self))
        #self.admin_user = admin_user

    def get_token(self):
        url = self.url + '/api/auth/get_tokens'

        #response = requests.get(url, auth=self.auth)
        #response = requests.post(url='https://erste-staging-pr-19.herokuapp.com/api/auth/get_tokens',auth=self.auth,headers=self.headers,)
        print ("********** requests **********")
        payload = {'username':'admin', 'password':'admin'}
        response = requests.post('https://erste-staging-pr-19.herokuapp.com/api/auth/get_tokens',auth=('admin', 'admin'))
        print ("********** response **********")
        print (response.text)
        print (response.url)
        #print (response.json())
        #print ("********** response **********")
        #print (response)
        #return response.json()
        return 0

