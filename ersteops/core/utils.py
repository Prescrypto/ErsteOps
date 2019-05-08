# -*- encoding: utf-8 -*-
import json
import base64
import logging
import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings
from django.contrib import messages

# Load Logging definition, this is defined in settings.py in the LOGGING section
logger = logging.getLogger('django_info')


TIMEOUT_TOLERANCE = 25

#Debug logger use this instead of print for debug in develop
def logger_debug(title="title",message="msg"):
    ''' Function to print debug loggers just with DEBUG True'''
    if settings.DEBUG:
        logger.info(title)
        logger.info(message)


# Calculate event duration
def eventDuration(start_duration,end_duration):
    return end_duration - start_duration

# Get odoo results
def get_odoo_call_result(url,payload,header,caller):
    result = { 'results': [] }
    try:
        response = requests.get(url, json=payload, headers=header)
        result = response.json()
        logger_debug("DEBUG Get by " + caller,str(response.json()).encode('utf-8'))
        logger.info('[SUCCESS OdooApi -> ' + caller + ']')
    except Exception as e:
        logger_debug("DEBUG: " + caller + " ERROR!",e)
        logger_debug("DEBUG: " + caller + " ERROR!",response)
        logger.error("[ERROR OdooApi -> " + caller + "]")
        logger.error(e)    
    return result   

class OdooApi(object):

    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger('django_info')
        #self.auth = HTTPBasicAuth(settings.ODOO_USERNAME, settings.ODOO_PASSWORD)
        self.url = settings.BASE_URL + settings.ODOO_URL
        self.headers = {"Content-Type": "text/html"}

    # Get Token
    def get_token(self):
        url = self.url + '/api/auth/get_tokens/'
        payload = {'username': settings.ODOO_USERNAME, 'password': settings.ODOO_PASSWORD}
        result = {'access_token': None}
        try:
            response = requests.post(url, data=json.dumps(payload), headers=self.headers, timeout=TIMEOUT_TOLERANCE)
            result = response.json()
            logger_debug("DEBUG: Get token succesfully",str(response.json()).encode('utf-8'))
            logger.info('[SUCCESS OdooApi -> get_token]')
        except Exception as e:
            logger_debug("DEBUG: Get token ERROR!",e)
            logger_debug("DEBUG: Get token ERROR!",response)
            logger.error("[ERROR OdooApi -> get_token]")
            logger.error(e)
        return result


    # Get patients matching string name (* in use)
    def get_by_patient_name(self,patient,access_token):
        url = self.url + '/api/res.partner/'
        payload = {"filters": "[(\"name\", \"ilike\", \"{}\")]".format(patient)}
        #payload = {"filters": "[(\"name\", \"ilike\", \"{}\"),(\"user_active\",\"=\",\"1\")]".format(patient)}
        header = {"Access-Token": access_token,"Content-Type":"text/html"}
        caller = "get_by_patient_name"
        return get_odoo_call_result(url,payload,header,caller)


    # Get patients matching string id (* in use)
    def get_like_patient_id(self,patient,access_token):
        url = self.url + '/api/res.partner/'
        payload = {"filters": "[(\"id\", \"=\", \"{}\")]".format(patient)}
        #payload = {"filters": "[(\"name\", \"ilike\", \"{}\"),(\"user_active\",\"=\",\"1\")]".format(patient)}
        header = {"Access-Token": access_token,"Content-Type":"text/html"}
        caller = "get_like_patient_id"
        return get_odoo_call_result(url,payload,header,caller)


    # Get patients matching string street
    def get_by_patient_street(self,patient,access_token):
        url = self.url + '/api/res.partner/'
        payload = {"filters": "[(\"street\", \"ilike\", \"{}\")]".format(patient)}
        header = {"Access-Token": access_token,"Content-Type":"text/html"}
        response = requests.get(url, json=payload, headers=header)
        return response.json()

    # Get patient by odoo id
    def get_by_patient_id(self,patient_id,access_token):
        url = self.url + '/api/res.partner/' + patient_id + '/'
        header = {"Access-Token": access_token,"Content-Type":"text/html"}
        response = requests.get(url,headers=header)
        logger_debug("From odoo api, patient_id",str(response.json()).encode('utf-8'))
        return response.json()

    # Get all odoo clients
    def get_by_all(self,patient_id,access_token):
        url = self.url + '/api/res.partner'
        #payload = {'id': patient_id}
        header = {"Access-Token": access_token,"Content-Type":"text/html"}
        response = requests.get(url,headers=header)
        return response.json()

    # Get company members by matching string name (* in use)
    def get_by_company_member(self,patient,access_token):
        url = self.url + '/api/company.member/'
        #payload = {"filters": "[(\"name\", \"ilike\", \"{}\")]".format(patient)}
        payload = {"filters": "[(\"name\", \"ilike\", \"{}\"),(\"user_active\" ,\"=\",1)]".format(patient)}
        header = {"Access-Token": access_token,"Content-Type":"text/html"}
        caller = "get_by_company_member"
        return get_odoo_call_result(url,payload,header,caller)

    # Get family memberes by matching string name (* in use)
    def get_by_family_member(self,patient,access_token):
        url = self.url + '/api/family.member/'
        #payload = {"filters": "[(\"name\", \"ilike\", \"{}\")]".format(patient)}
        #payload = {"filters": "[(\"name\", \"ilike\", \"{}\"),(\"user_active\",\"=\",true)]".format(patient)}
        payload = {"filters": "[(\"name\", \"ilike\", \"{}\"),(\"user_active\" ,\"=\",1)]".format(patient)}
        header = {"Access-Token": access_token,"Content-Type":"text/html"}
        caller = "get_by_family_member"
        return get_odoo_call_result(url,payload,header,caller)

    # Get company member by id
    def get_by_company_member_id(self,patient_id,access_token):
        url = self.url + '/api/company.member/' + patient_id + '/'
        header = {"Access-Token": access_token,"Content-Type":"text/html"}
        response = requests.get(url,headers=header)
        return response.json()

    # Get family member by id
    def get_by_family_member_id(self,patient_id,access_token):
        url = self.url + '/api/family.member/' + patient_id + '/'
        header = {"Access-Token": access_token,"Content-Type":"text/html"}
        response = requests.get(url,headers=header)
        return response.json()
