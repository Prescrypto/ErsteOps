# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
import json
import datetime
import requests
from requests.auth import HTTPBasicAuth
# Django utils
from django.shortcuts import render,redirect
from django.views.generic import View, CreateView, ListView, DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse
from django.db.models import Q
# Our models
from core.utils import OdooApi
from .utils import JSONResponseMixin, AjaxableResponseMixin, UpdateJsonResponseMixin
from .forms import OdooClientForm, OdooClientAuto
from .models import Emergency,AttentionDerivation, AttentionKind, AttentionHospital, EmergencyDerivation
from unit.models import Unit
from unit.utils import UNIT_LIST_FIELD
from .list_fields import EMERGENCY_LIST_FIELDS, HOSPITAL_LIST_FIELDS
from .helpers import get_copago

from django import template

from django.conf import settings

from twilio.rest import Client 


# Logging library
import logging
# Load Logging definition, this is defined in settings.py in the LOGGING section
logger = logging.getLogger('django_info')

@csrf_exempt
def grade_view(request):
    ''' '''
    bad_response = JsonResponse({'status':'bad request'})
    bad_response.status_code = 400

    if not request.is_ajax():
        return bad_response
    if not request.body:
        return bad_response

    data = json.loads(request.body.decode('utf-8'))
    if 'id' in data and 'attention_final_grade' in data and 'attention_justification' in data:
        try:
            emergency = Emergency.objects.get(id=data['id'])
            attention_kind = AttentionKind.objects.get(grade_type=data['attention_final_grade'])
            emergency.attention_final_grade = attention_kind
            emergency.attention_justification = data['attention_justification']
            emergency.save()
            data.update({'status': 'success', 'client_id':emergency.odoo_client})
            response = JsonResponse(data)
            response.status_code = 202
            return response
        except Exception as e:
            logger.error("[Grade View ERROR]: {}, type: {}".format(e, type(e)))
            return bad_response

    else:
        return bad_response

# Update Timer Functionality
@csrf_exempt
def timer_view(request):
    ''' Update emergency timer when option selected in FE'''
    bad_response = JsonResponse({'status':'bad request'})
    bad_response.status_code = 400

    if not request.is_ajax():
        return bad_response
    if not request.body:
        return bad_response

    data = json.loads(request.body.decode('utf-8'))

    if 'id' in data and 'timer_type' in data :
        try:
            emergency = Emergency.objects.get(id=data['id'])
            if data['timer_type'] == '1':
                emergency.unit_dispatched_time = timezone.now()
            if data['timer_type'] == '2':
                emergency.arrival_time = timezone.now()
                emergency.attention_time = timezone.now()
            if data['timer_type'] == '3':
                emergency.derivation_time = timezone.now()
            if data['timer_type'] == '4':
                emergency.patient_arrival = timezone.now()

            emergency.save()
            data.update({'status': 'success', 'client_id':emergency.odoo_client})
            response = JsonResponse(data)
            response.status_code = 202
            return response
        except Exception as e:
            logger.error("[Update Timer View ERROR]: {}, type: {}".format(e, type(e)))
            return bad_response

    else:
        return bad_response
# /Update Timer Functionality

# Update Derivation Functionality
@csrf_exempt
def derivation_view(request):
    ''' '''
    bad_response = JsonResponse({'status':'bad request'})
    bad_response.status_code = 400

    if not request.is_ajax():
        return bad_response
    if not request.body:
        return bad_response

    data = json.loads(request.body.decode('utf-8'))

    if 'id' in data and 'timer_type' in data :
        try:
            emergency = Emergency.objects.get(id=data['id'])
            # if data['timer_type'] == '1':
            #     emergency.unit_dispatched_time = timezone.now()
            # if data['timer_type'] == '2':
            #     emergency.arrival_time = timezone.now()
            #     emergency.attention_time = timezone.now()
            # if data['timer_type'] == '3':
            #     emergency.derivation_time = timezone.now()
            # if data['timer_type'] == '4':
            #     emergency.patient_arrival = timezone.now()

            # emergency.save()
            data.update({'status': 'success', 'client_id':emergency.odoo_client})
            response = JsonResponse(data)
            response.status_code = 202
            return response
        except Exception as e:
            logger.error("[Update Derivation View ERROR]: {}, type: {}".format(e, type(e)))
            return bad_response

    else:
        return bad_response
# /Update Derivation Functionality

@method_decorator(csrf_exempt, name='dispatch')
class EmergencyNew(AjaxableResponseMixin, CreateView):
    template_name = "emergency/new.html"
    model = Emergency
    fields = EMERGENCY_LIST_FIELDS
    success_url = 'emergencydashboard'


# Return Emergency data for selected item in dashboard
class EmergencyJSONView(JSONResponseMixin, DetailView):
    ''' Custom Json View for Emergency details '''
    model = Emergency

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)


# Display FE Dashboard 
@method_decorator(login_required, name='dispatch')
class EmergencyDashboardList(ListView):
    template_name = "emergency/dashboard.html"
    model = Emergency

    def get_context_data(self, **kwargs):
        active_emergencies = Emergency.objects.filter(is_active=True).count()
        units = Unit.objects.available_units()
        #hospitals = AttentionHospital.objects.all()
        hospitals_lists = serializers.serialize('json',list(AttentionHospital.objects.all()),fields=HOSPITAL_LIST_FIELDS)
        available_units_counter = units.count()
        units_list = serializers.serialize('json', list(units), fields=UNIT_LIST_FIELD)
        context = super(EmergencyDashboardList, self).get_context_data(**kwargs)
        context.update({
            'now': timezone.now(),
            'active_emergencies': active_emergencies,
            'available_units_counter': available_units_counter,
            'units_list': units_list,
            'hospitals': hospitals_lists,
        })
        return context

    def get_queryset(self):
        fields = EMERGENCY_LIST_FIELDS
        data = serializers.serialize('json', list(Emergency.objects.filter(is_active=True)), fields=fields, use_natural_foreign_keys=True, use_natural_primary_keys=True)
        logger.info('[Dashboard List Sent SUCCESS')
        #print("{}".format(data))
        return data



@method_decorator(csrf_exempt, name='dispatch')
class EmergencyJSONUpdate(UpdateJsonResponseMixin, UpdateView):
    #template_name = "emergency/update.html"
    model = Emergency
    fields = EMERGENCY_LIST_FIELDS
    success_url = 'emergencydashboard'



class EmergencyJSONGetPatient(View):
    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            ''' Connect to api and return json data'''
            data = handle_patient_data(kwargs['patient_id'])
            return JsonResponse(data)


def handle_patient_data(patient_id):
    ''' Method who handle patient data '''
    target_id = patient_id
    # Extract patient_id
    # Target 000129000001000129
    # First 6 digits patient_id
    # Second 6 digits source_id: 1 res.partner,2 family.member, 3 company.member
    # Third 6 digits parent_id
    patient_id = int(target_id[:6])
    # Extract where the patient been found
    source_id = int(target_id[6:-6])
    # Initialize Odoo api
    _api_odoo = OdooApi()
    # Get Token
    result = _api_odoo.get_token()
    # Case when Patient in res.partner
    if source_id == 1:
        patient_data = _api_odoo.get_by_patient_id( str(patient_id),result['access_token'])
        parent_data = {}
    # Case when Patient in family.member
    elif source_id == 2:
        patient_data = _api_odoo.get_by_family_member_id( str(patient_id),result['access_token'])
        parent_data = _api_odoo.get_by_patient_id( str(patient_data['parent_id']['id']),result['access_token'])
    # Case when Patient in company.member
    elif source_id == 3:
        patient_data = _api_odoo.get_by_company_member_id( str(patient_id),result['access_token'])
        parent_data = _api_odoo.get_by_patient_id( str(patient_data['parent_id']['id']),result['access_token'])

    return patient_json(source_id, patient_data, parent_data)


# Resume and clean patient and partner data
def patient_json(source_id,patient_data,parent_data):
    patient_data_json = {}
    try:
        if source_id == 1:
            patient_data_json = {
                "id_odoo_client" : patient_data['reference_id'] if patient_data.get('reference_id', 'None') != None else "Sin ID",
                "id_patient_name" : "{}".format(patient_data['name']),
                "id_patient_allergies" : '',
                "id_patient_illnesses" : '',
                "id_caller_relation": '',
                "id_patient_age": 0,
                "id_zone": str(patient_data['zone']).upper(),
                "id_subscription_type": get_subscription_plan(patient_data.get('client_type','N/A'),patient_data.get('comment',None)),
                "addresses": address_json(patient_data,patient_data),
                "min_addresses": min_address_json(patient_data,patient_data),
                "copago_amount": get_copago(patient_data.get('copago_amount', 0)),
                "has_paid" : patient_data.get('outstanding', False),
                "erste_code": patient_data.get('group_code','Sin Id'),
                "id_tel_local":patient_data.get('phone','N/A'),
                "id_tel_mobile":patient_data.get('mobile','N/A'),
                "id_partner_name":patient_data.get('name','N/A'),
                "id_partner_legalname":patient_data.get('legal_name','N/A'),
                "id_sales_rep":patient_data.get('sales_rep'),
                #"comment": patient_data['comment'],
            }
        else:
            patient_data_json ={
                "id_odoo_client" : parent_data['reference_id'] if parent_data.get('reference_id', 'None') != None else "Sin ID",
                "id_patient_name" : "{} ({})".format(patient_data['name'], parent_data['name']),
                "id_patient_allergies" : patient_data['allergies'],
                "id_patient_illnesses" : patient_data['prev_ailments'],
                "id_caller_relation" : partner_relationship(source_id,patient_data['relationship']),
                "id_patient_age": patient_age(patient_data['birthday']),
                "id_zone": str(parent_data['zone']).upper(),
                "id_subscription_type": get_subscription_plan(parent_data.get('client_type','N/A'),patient_data.get('comment',None)),
                "addresses": address_json(parent_data,patient_data),
                "min_addresses": min_address_json(parent_data,patient_data),
                "copago_amount": get_copago(parent_data.get('copago_amount', 0)),
                "has_paid" : parent_data.get('outstanding', False),
                "erste_code": parent_data.get('group_code','Sin Id'),
                "id_tel_local":patient_data.get('phone','N/A'),
                "id_tel_mobile":patient_data.get('mobile','N/A'),
                "id_partner_name":parent_data.get('name','N/A'),
                "id_partner_legalname":parent_data.get('legal_name','N/A'),
                "id_sales_rep":patient_data.get('sales_rep'),
                #"comment": patient_data['comment'],
            }
        logger.info('[ GET PATIENTJSON FOR FILLUP EMERGENCY FORM SUCCESS ]')
    except Exception as e:
        logger.error("DEBUG: patient_json ERROR!")
        logger.error("GET PATIENTJSON FOR FILLUP EMERGENCY FORM ERROR! ")
        logger.error(e)      
    return patient_data_json


def get_subscription_plan(client_type,subscription_plan):
    '''Get client type from odoo , translates to spanish equivalent and add subscription plan from odoo comment field'''
    subscription_plan = " - Plan: " + subscription_plan if subscription_plan != None else ' Plan: N/A' 
    client_plan='N/A'

    if client_type == 'company':
        client_plan = 'Compañia'
    if client_type == 'family':
        client_plan = 'Familia'
    if client_type == 'private':
        client_plan = 'Privado'
    return client_plan + subscription_plan


def partner_relationship(source_id,patient_relation):
    RELATIONSHIP_CODES_FAMILY = {
        "1": "Padre",
        "2": "Madre",
        "3": "Esposo/a",
        "4": "Descendiente",
        "5": "Otro Familiar",
    }
    RELATIONSHIP_CODES_COMPANY = {
        "1": "Dueño",
        "2": "Director",
        "3": "Ejecutivo",
        "4": "Administrador",
        "5": "Empleado",
        "6": "Otro",
    }
    relationship = ""
    if source_id == 2:
        relationship = RELATIONSHIP_CODES_FAMILY.get(patient_relation,"No clasificado")
    elif source_id ==3:
        relationship = RELATIONSHIP_CODES_COMPANY.get(patient_relation,"No clasificado")
    return relationship

def patient_age(birthday):
    # dt = datetime.strptime(birthday,"%Y -%b-%d")
    # age = datetime.date.today() - dt
    #return age.year
    return datetime.date.today().year - int(birthday[:4])

def address_json(parent_data,patient_data):
    adress_list = []
    #adresses_json = {}
    if len(parent_data['child_ids']) >=1:
        for address in parent_data['child_ids']:
            if address['type'] == 'coverage':
                adresses_json = {
                    "id_address_id": address['id'],
                    "id_address_street": address['street'],
                    "id_address_extra": address['street2'],
                    "id_address_zip_code": address['zip'],
                    "id_address_county": address['sat_municipio_id']['nombre_municipio'],
                    "id_address_col": address['sat_colonia_id']['nombre_colonia'],
                    "id_address_between": address['cross_street'],
                    "id_address_and_street": address['crosses_with'],
                    "id_address_ref": address['references'],
                    "id_address_front": address['exterior'],
                    "id_address_instructions": address['details'],
                    "id_address_notes": address['comment']
                }
                adress_list.append(adresses_json)
    if len(adress_list) == 0:
        adresses_json = {
                    "id_address_id": "1",
                    "id_address_street": parent_data['street'],
                    "id_address_extra": parent_data['street2'],
                    "id_address_zip_code": parent_data['zip'],
                    "id_address_county": '',
                    "id_address_col": '',
                    "id_address_between": '',
                    "id_address_and_street": '',
                    "id_address_ref": '',
                    "id_address_front": '',
                    "id_address_instructions": '',
                    "id_address_notes": '',
        }
        adress_list.append(adresses_json)
    data = json.dumps(adress_list)
    return data

def min_address_json(parent_data,patient_data):
    adress_list = []
    #adresses_json = {}
    if len(parent_data['child_ids']) >=1:
        for address in parent_data['child_ids']:
            if address['type'] == 'coverage':
                adresses_json = {
                    "id_address_id": address['id'],
                    "id_address_street": address['street'],
                }
                adress_list.append(adresses_json)
    if len(adress_list) == 0:
        adresses_json = {
                    "id_address_id": "1",
                    "id_address_street": parent_data['street'],
        }
        adress_list.append(adresses_json)

    return adress_list

@method_decorator(login_required, name='dispatch')
class EmergencyActivate(View):
    def get(self, request, *args, **kwargs):
        patient_id = kwargs['patient_id']
        try:
            emergency = Emergency.objects.get(id=patient_id)
        except:
            return redirect('/emergency/list/')
        if emergency.is_active:
            emergency.is_active = False
        else:
            emergency.is_active = True
        emergency.save()
        return redirect('/emergency/list/')

# Whatsapp text output generator
class EmergencyText(View):
    def get(self, request, *args, **kwargs):
        emergency_id = kwargs['emergency_id']
        try:
            emergency = Emergency.objects.get(id=emergency_id)
            #content = str(emergency.id)
            content_patient = "*No_Emergencia:* _%s_, *Paciente:* _%s_, *Genero:* _%s_, *Edad:* _%s_, *Alergias:* _%s_, *Enfermedades:* _%s_, *Notas:* _%s_, *Sintomas:* _%s_,"%(
                emergency.id,
                emergency.patient_name,
                emergency.patient_gender,
                emergency.patient_age,
                emergency.patient_allergies,
                emergency.patient_illnesses,
                emergency.patient_notes,
                emergency.main_complaint,
                )

            content_service = " *Categoria_Servicio:* _%s_, *Grado:* _%s_, *Zona:* _%s_."%(

                emergency.service_category,
                emergency.grade_type,
                emergency.zone.name,

                )
            content_address = " *Direccion:* _%s_, _%s_, *C.P.:* _%s_, *Delegacion:* _%s_, *Colonia:* _%s_, *Entre la calle:* _%s_ *y* %s, *Referencias:* _%s_, *Fachada:* %s, *Instruccciones llegada:* _%s_" % (
                emergency.address_street,
                emergency.address_extra,
                emergency.address_zip_code,
                emergency.address_county,
                emergency.address_col,
                emergency.address_between,
                emergency.address_and_street,
                emergency.address_ref,
                emergency.address_front,
                emergency.address_instructions,
                )
            content_paperless="*Parte_Medico:* {}/paperless/new/{}/".format(settings.PAPERLESS_URL,emergency.id)
            #for unit in emergency.units.all():
            #    content_paperless += "*Parte_Medico:* http://{}/{}".format(unit)
            logger.info("PAPERLESS DATA")    
            logger.info(content_paperless)

            content = content_patient + content_address + content_service + content_paperless
            # twillio_whatsap_send(content_paperless)

        #except:
        except Exception as e:
            logger.error("DEBUG: WHATSAPP NOTIFY ERROR!")
            logger.error("ERROR FORMATING MESSAGE ERROR! ")
            logger.error(e) 
            content = "Emergencia no encontrada!"

        return HttpResponse(content, content_type='text/plain')

class EmergencyEnd(View):
    def get(self, request, *args, **kwargs):
        patient_id = kwargs['patient_id']
        try:
            emergency = Emergency.objects.get(id=patient_id)
        except:
            logger.error("[EmergencyEnd] Not found emergency with patient id")
            return redirect('/emergency/dashboard/')
        emergency.is_active = False
        emergency.final_emergency_time = timezone.now()
        emergency.save()
        logger.info('Emergency Stop! ID:{}'.format(emergency.id))
        return redirect('/emergency/dashboard/')


class EmergencyJsonEnd(View):
    def get(self, request, *args, **kwargs):
        patient_id = kwargs['patient_id']
        try:
            emergency = Emergency.objects.get(id=patient_id)
        except:
            logger.error("[Error EmergencyJsonEnd] Not found emergency with patient id")
            return HttpResponse(status=404)
        emergency.is_active = False
        emergency.final_emergency_time = timezone.now()
        for unit in emergency.units.all():
            unit.is_assigned = False
            unit.save()
        emergency.save()
        logger.info("[Success EmergencyJsonEnd] Deactivate emergency with id: {}".format(emergency.id))
        return HttpResponse(status=200)


@method_decorator(login_required, name='dispatch')
class OdooSubscription(View):
    template_name = "emergency/search_odoo_auto.html"
    def get(self, request, *args, **kwargs):
        form = OdooClientAuto
        return render(request, self.template_name,{"form": form})



BAD_REQUEST = HttpResponse(json.dumps({'error': 'Bad Request'}), status=400, content_type='application/json')

def hospital_json_list(request):
    ''' List Json View for local available Hospitals '''
    if request.is_ajax():
        hospitals = AttentionHospital.objects.all()
        data = serializers.serialize('json', list(hospitals), fields=HOSPITAL_LIST_FIELDS)
        _raw_data = json.loads(data)
        # for unit in _raw_data:
        #     if unit['fields']['is_alliance']:
        #         unit['fields'].update({'identifier': '{}{}'.format(unit['fields']['identifier'],' (Alianza)')})
        #     else:
        #         continue
        logger.info("[Success HospitaljsonEnd] {}".format(json.dumps(_raw_data)))
        return HttpResponse(json.dumps(_raw_data), content_type='application/json', status=200)
    else:
        return BAD_REQUEST



def twillio_whatsap_send(msg_content):
    account_sid = '' 
    auth_token = '' 
    client = Client(account_sid, auth_token) 
    #sandbox
    send_from_number = 'whatsapp:+14155238886'
    #personal twillio number
    #send_from_number = 'whatsapp:+18456403579'

    try:
        # message = client.messages.create( 
        #                       from_= send_from_number,  
        #                       body = msg_content,      
        #                       to = 'whatsapp:+5215591984288' 
        #                   ) 
        #print(message.sid)

        #from twilio.rest import Client 
 
        #account_sid = 'AC3af5fc2897080852175755b01fe86592' 
        #auth_token = '[AuthToken]' 
        client = Client(account_sid, auth_token) 
 
        message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your Yummy Cupcakes Company order of 1 dozen frosted cupcakes has shipped and should be delivered on July 10, 2019. Details: {}'.format(msg_content),      
                              to='whatsapp:+5215591984288' 
                          ) 
 
       # print(message.sid)

        logger.info('[ WHATSAPP MESSAGE SUCCESS ]')
        logger.info('[ Twillio response: {}'.format(message.sid))
    except:
        logger.error("DEBUG: WHATSAPP NOTIFY ERROR!")
        logger.error(e)

    #logger.info("[Success EmergencyJsonEnd] Deactivate emergency with id: {}".format(emergency.id))
    return message.sid
