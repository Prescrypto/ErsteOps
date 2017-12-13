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


#tree.csv
def readcsv(filename, delimiter=","):
    import csv
    ifile = open(filename, "rU")
    reader = csv.reader(ifile, delimiter=delimiter)
    a = []
    for row in reader:
        a.append (row)
    ifile.close()
    return a

def tree_to_models():
    from emergency.models import Symptom2
    rows=readcsv("tree.csv")
    rowFirst=True
    for row in rows:
        claves=row[0].split(".")
        if len(claves) == 1 and claves[0].isdigit():
            parent=False
        elif len(claves)>1:
            try:
                parent=Symptom2.objects.get(clave=row[0][:row[0].rfind('.')])
            except Exception as e:
                parent=False

        if not Symptom2.objects.filter(clave=row[0]).exists() and not rowFirst:
            children=Symptom2.objects.create(
                clave=str(row[0]),
                name=unicode(row[9].lstrip(), errors='ignore'),
                grado=str(row[10]),
                n1 = row[1] if row[1] else "0",
                n2 = row[2] if row[2] else "0",
                n3 = row[3] if row[3] else "0",
                n4 = row[4] if row[4] else "0",
                n5 = row[5] if row[5] else "0",
                n6 = row[6] if row[6] else "0",
                n7 = row[7] if row[7] else "0",
                nivel = row[8] if row[8] else "0",
            )
            #children
            if parent:
                parent.children.add(children)

        rowFirst=False
