
# Python libs
import json
import logging
# Django libs
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Our methods
from core.utils import OdooApi #, logger_debug

# Load Logging definition, this is defined in settings.py in the LOGGING section
logger = logging.getLogger('django_info')

# Use this to check if the search can be made by client id
def num(s):
    try:
        return int(s)
    except ValueError:
        return 0

# Create your views here.
def get_subscriptor(request):
    if request.is_ajax():
        # Ini Odoo api
        _api_odoo = OdooApi()
        # Get Access token
        result = _api_odoo.get_token()
        q = request.GET.get('term', '')
        # Check if access token is exist!
        if result['access_token']:
            #################
            # Get info from res.partner
            patients = _api_odoo.get_by_patient_name(q, result['access_token'])
            clients = patients['results']
            #logger_debug("******** Find in Clients ********",clients)

            # get info from family.member
            family_members = _api_odoo.get_by_family_member(q, result['access_token'])
            clients_family = family_members['results']
            #logger_debug("******** Find in Family Members ********",clients_family)

            # get info from company.member
            company_members = _api_odoo.get_by_company_member(q, result['access_token'])
            clients_company = company_members['results']
            #logger_debug("******** Find in Company Members ********",clients_company)

            #get client by erste id
            #first convert q to integer
            q_int = num(q)
            if q_int != 0:
                client_by_id = _api_odoo.get_like_patient_id(q, result['access_token'])
                clients_by_id = client_by_id['results']
            else:
                clients_by_id = []
            #logger_debug("******** Find in clients by id ********",clients_by_id)
            ##################
        else:
            clients = []
            clients_family = []
            clients_company = []
            clients_by_id = []
        # Init result list
        results = []
        # Add res.partner data
        for client in clients:
            if client.get('client_type', None) is None:
                continue

            client_export_id_label= client['reference_id'] if client.get('reference_id', 'None') != 'None' else "Sin ID"
            client_json = {
                "id": client['id'],
                "label": "{} -({}) Id: {}".format(client['name'], str(client["client_type"]), client_export_id_label),
                "value": "{} -({}) Id: {}".format(client['name'], str(client["client_type"]), client_export_id_label),
                "parent_id": client['id'],
                "client_type": client['client_type'],
                "source": 'res.partner',
                "client_export_id": client['reference_id'],
                "target": str(client['id']).zfill(6) + str(1).zfill(6) + str(client['id']).zfill(6)
            }
            results.append(client_json)

        # Add res.partner data by id
        for client in clients_by_id:
            if client.get('client_type', None) is None:
                continue

            client_export_id_label= client['reference_id'] if client.get('reference_id', 'None') != 'None' else "Sin ID"
            client_json = {
                "id": client['id'],
                "label": "{} -({}) Id: {}".format(client['name'], str(client["client_type"]), client_export_id_label),
                "value": "{} -({}) Id: {}".format(client['name'], str(client["client_type"]), client_export_id_label),
                "parent_id": client['id'],
                "client_type": client['client_type'],
                "source": 'res.partner',
                "client_export_id": client['reference_id'],
                "target": str(client['id']).zfill(6) + str(1).zfill(6) + str(client['id']).zfill(6)
            }
            results.append(client_json)

        # Add family.member
        for client in clients_family:
            client_export_id_label = client['parent_id']['reference_id'] if client['parent_id'].get('reference_id', 'None') != 'None' else "Sin ID"
            parent_name =  client['parent_id']['name']
            client_json = {
                "id": client['id'],
                "label": "{} -(Miembro Familiar - Titular: {}) Id: {}".format(client['name'], parent_name, client_export_id_label),
                "value": "{} -(Miembro Familiar - Titular: {}) Id: {}".format(client['name'], parent_name, client_export_id_label),
                "parent_id": client['parent_id']['id'],
                "parent_name": parent_name, # Titular Name
                "client_export_id": client['parent_id']['reference_id'],
                "client_type": 'family_member',
                "source": 'family.member',
                "target": str(client['id']).zfill(6) + str(2).zfill(6) + str(client['parent_id']['id']).zfill(6)
            }
            results.append(client_json)

        # Add company.member
        for client in clients_company:
            client_export_id_label = client['parent_id']['reference_id'] if client['parent_id'].get('reference_id', 'None') != 'None' else "Sin ID"
            parent_name_label = client['parent_id']['name'] if client['parent_id']['name'] != "" else client['parent_id'].get('legal_name', "No Asignado")
            client_json = {
                "id": client['id'],
                "label": "{} -(Miembro Afiliado - Empresa: {}) Id: {}".format(client['name'], parent_name_label, client_export_id_label),
                "value": "{} -(Miembro Afiliado - Empresa: {}) Id: {}".format(client['name'], parent_name_label, client_export_id_label),
                "parent_id": client['parent_id']['id'],
                "parent_name": client['parent_id']['name'], # Nombre de fantasia
                "parent_legal_name": client['parent_id']['legal_name'], # Nombre Legal
                "client_export_id": client['parent_id']['reference_id'],
                "client_type": "company_member",
                "source": 'company.member',
                "target": str(client['id']).zfill(6) + str(3).zfill(6) + str(client['parent_id']['id']).zfill(6)
            }
            results.append(client_json)

        data = json.dumps(results)
        #logger_debug("******** Final Results ********", data)
        logger.info('[SUCCESS AjaxApiReturn]')
    else:
      logger.error("[ERROR Subscriptor ajaxview] Request no Valido")
      data = 'fail!'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
