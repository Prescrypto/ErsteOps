from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json
from core.utils import OdooApi
# Logging library
import logging
# Load Logging definition, this is defined in settings.py in the LOGGING section
logger = logging.getLogger('django_info')

# Create your views here.
def get_subscriptor(request):
    if request.is_ajax():
        # Ini Odoo api
        _api_odoo = OdooApi()
        # Get Access token
        result = _api_odoo.get_token()
        q = request.GET.get('term', '')

        # Get info from res.partner
        patients = _api_odoo.get_by_patient_name( q,result['access_token'])
        clients = patients['results']
        logger.info('%s (%s)' % ('AjaxApi_partner',clients))

        # get info from family.member
        famiily_members = _api_odoo.get_by_family_member( q,result['access_token'])
        clients_family = famiily_members['results']
        logger.info('%s (%s)' % ('AjaxApi_family',famiily_members))

        # get info from company.member
        company_members = _api_odoo.get_by_company_member( q,result['access_token'])
        clients_company = company_members['results']
        logger.info('%s (%s)' % ('AjaxApi_company',company_members))

        # Init result list
        results = []
        # Add res.partner data 
        for client in clients:
            client_json = {
                "id": client['id'],
                "label": client['name'] + ' - (' + client['client_type'] + ')',
                "value": client['name'] + ' - (' + client['client_type'] + ')',
                "parent_id": client['id'],
                "client_type": client['client_type'],
                "source": 'res.partner',
            }
            results.append(client_json)

        # Add family.member
        for client in clients_family:
            client_json = {
                "id": client['id'],
                "label": client['name'] + ' - ( ' + str(client['id']) + ' - ' + 'Family Member' + ')',
                "value": client['name'] + ' - ( ' + str(client['id']) + ' - ' + 'Family Member' + ')',
                "parent_id": client['parent_id']['id'],
                "client_type": 'family_member',
                "source": 'family.member'
            }
            results.append(client_json)

        # Add company.member
        for client in clients_company:
            client_json = {
                "id": client['id'],
                "label": client['name'] + ' - ( ' + str(client['id']) + ' - ' + 'Company Member' + ')',
                "value": client['name'] + ' - ( ' + str(client['id']) + ' - ' + 'Company Member' + ')',
                "parent_id": client['parent_id']['id'],
                "client_type": "company_member",
                "source": 'company.member'
            }
            results.append(client_json)

        data = json.dumps(results)
        logger.info('%s (%s)' % ('AjaxApiReturn',data))
    else:
      data = 'fail!'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
