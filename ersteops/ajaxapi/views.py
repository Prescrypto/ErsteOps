from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json
from core.utils import OdooApi

# Create your views here.
def get_subscriptor(request):
    my_session=request.session['resultodoo']
    if request.is_ajax():
        # Ini Odoo api
        _api_odoo = OdooApi()
        # Get Access token
        result = _api_odoo.get_token()
        q = request.GET.get('term', '')
        patients = _api_odoo.get_by_patient_name( q,result['access_token'])
        clients = patients['results']
        print("******** ajax *******")
        print(clients)
        #data = session['access_token']
        results = []
        for client in clients:
            client_json = {}
            client_json['id'] = client['id']
            client_json["label"] = client['name']
            client_json["value"] = client['name']
            client_json['id_client_id'] = client['id']
            results.append(client_json)
        data = json.dumps(results)
        print(data)
    else:
      data = 'fail!'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
