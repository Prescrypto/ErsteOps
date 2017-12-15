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

    def get_by_patient_name(self,patient,access_token):
        url = self.url + '/api/res.partner/'
        payload = {"filters": "[(\"name\", \"ilike\", \"{}\")]".format(patient)}
        header = {"Access-Token": access_token,"Content-Type":"text/html"}
        response = requests.get(url, json=payload, headers=header)
        return response.json()

    def get_by_patient_street(self,patient,access_token):
        url = self.url + '/api/res.partner/'
        payload = {"filters": "[(\"street\", \"ilike\", \"{}\")]".format(patient)}
        header = {"Access-Token": access_token,"Content-Type":"text/html"}
        response = requests.get(url, json=payload, headers=header)
        return response.json()

    def get_by_patient_id(self,patient_id,access_token):
        url = self.url + '/api/res.partner/' + patient_id + '/'
        header = {"Access-Token": access_token,"Content-Type":"text/html"}
        response = requests.get(url,headers=header)
        return response.json()

    def get_by_all(self,patient_id,access_token):
        url = self.url + '/api/res.partner'
        #payload = {'id': patient_id}
        header = {"Access-Token": access_token,"Content-Type":"text/html"}
        response = requests.get(url,headers=header)
        return response.json()

