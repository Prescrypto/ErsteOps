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
        #payload = {'filters': "[('name','like','"+patient+"')]"}
        #payload = {"filters": "[(\"name\", \"like\", \"ompany\")]"}
        payload = {"filters": "[(\"name\", \"like\", \"{}\")]".format(patient)}
        header = {"Access-Token": access_token,"Content-Type":"text/html"}
        #response = requests.post(url, data=json.dumps(payload), headers=header)
        response = requests.get(url, json=payload, headers=header)
        print("********** patient ***********")
        print(patient)
        print("********** response **********")
        print(response)
        print("********** payload **********")
        print(payload)
        return response.json()

    def get_by_patient_street(self,patient,access_token):
        url = self.url + '/api/res.partner/'
        #payload = {'filters': "[('name','like','"+patient+"')]"}
        #payload = {"filters": "[(\"name\", \"like\", \"ompany\")]"}
        payload = {"filters": "[(\"street\", \"like\", \"{}\")]".format(patient)}
        header = {"Access-Token": access_token,"Content-Type":"text/html"}
        #response = requests.post(url, data=json.dumps(payload), headers=header)
        response = requests.get(url, json=payload, headers=header)
        print("********** patient ***********")
        print(patient)
        print("********** response **********")
        print(response)
        print("********** payload **********")
        print(payload)
        return response.json()

    def get_by_patient_id(self,patient_id,access_token):
        url = self.url + '/api/rest.partner/' + patient_id
        #payload = {'id': patient_id}
        header = {"Access-Token": access_token,"Content-Type":"text/html"}
        response = requests.get(url,headers=header)
        print("********** patient ***********")
        print(patient_id)
        print("********** response ***********")
        print(response)
        print("********** url ***********")
        print(response.url)
        return response.json()

