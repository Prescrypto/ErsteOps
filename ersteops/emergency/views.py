# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.views.generic import View, CreateView, ListView, DetailView, UpdateView
from emergency.models import Emergency,AttentionDerivation
from django.utils import timezone
from emergency.forms import OdooClientForm, OdooClientAuto
from core.utils import OdooApi
import requests
from requests.auth import HTTPBasicAuth
import json
import datetime
from django.core import serializers
# Logging library
import logging
# Load Logging definition, this is defined in settings.py in the LOGGING section
logger = logging.getLogger('django_info')

class EmergencyBlank(View):
    template_name = "emergency/blank.html"
    def get(self, request, *args, **kwargs):
        form=''
        return render(request, self.template_name,{"form": form})



class EmergencyNew(CreateView):
    template_name = "emergency/new.html"
    model = Emergency
    fields = ['id','odoo_client',
                'service_category',
                'grade_type',
                'zone',
                'start_time',
                'end_time',
                'is_active',
                'unit',
                'unit_assigned_time',
                'unit_dispatched_time',
                'arrival_time',
                'attention_time',
                'derivation_time',
                'hospital_arrival',
                'patient_arrival',
                'final_emergency_time',
                'address_street',
                'address_extra',
                'address_zip_code',
                'address_county',
                'address_col',
                'address_between',
                'address_and_street',
                'address_ref',
                'address_front',
                'address_instructions',
                'address_notes',
                'caller_name',
                'caller_relation',
                'patient_name',
                'patient_gender',
                'patient_age',
                'patient_allergies',
                'patient_illnesses',
                'patient_notes',
                'attention_final_grade',
                'attention_justification',
                'main_complaint',
                'complaint_descriprion',
                'subscription_type'
                ]
    success_url = '/emergency/list/'

class EmergencyListView(ListView):
    template_name = "emergency/list.html"
    model = Emergency
    def get_context_data(self, **kwargs):
        context = super(EmergencyListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class EmergencyDetailView(DetailView):
    template_name = "emergency/detail.html"
    model = Emergency
    def get_context_data(self, **kwargs):
        context = super(EmergencyDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class EmergencyDashboardList(ListView):
    template_name = "emergency/dashboard.html"
    model = Emergency
    def get_context_data(self, **kwargs):
        context = super(EmergencyDashboardList, self).get_context_data(**kwargs)
        context.update({
            'now': timezone.now(),
        })
        return context

    def get_queryset(self):
        fields = ('id','odoo_client',
                'service_category',
                'grade_type',
                'zone',
                'start_time',
                'end_time',
                'is_active',
                'unit',
                'unit_assigned_time',
                'unit_dispatched_time',
                'arrival_time',
                'attention_time',
                'derivation_time',
                'hospital_arrival',
                'patient_arrival',
                'final_emergency_time',
                'address_street',
                'address_extra',
                'address_zip_code',
                'address_county',
                'address_col',
                'address_between',
                'address_and_street',
                'address_ref',
                'address_front',
                'address_instructions',
                'address_notes',
                'caller_name',
                'caller_relation',
                'patient_name',
                'patient_gender',
                'patient_age',
                'patient_allergies',
                'patient_illnesses',
                'patient_notes',
                'attention_final_grade',
                'attention_justification',
                'main_complaint',
                'complaint_descriprion',
                'subscription_type'
                )
        emm_list = Emergency.objects.filter(is_active=True)
        data = serializers.serialize('json', list(emm_list), fields=fields)
        # TEMP remove later
        return data


class EmergencyDerivation(CreateView):
    template_name = "emergency/derivation.html"
    model = AttentionDerivation
    fields = ['emergency',
                'motive',
                'hospital',
                'eventualities',
                'reception',
                'notes',
        ]
    success_url = '/emergency/list/'

class EmergencyUpdate(UpdateView):
    template_name = "emergency/update.html"
    model = Emergency
    fields = ['id','odoo_client',
                'service_category',
                'grade_type',
                'zone',
                'start_time',
                'end_time',
                'is_active',
                'unit',
                'unit_assigned_time',
                'unit_dispatched_time',
                'arrival_time',
                'attention_time',
                'derivation_time',
                'hospital_arrival',
                'patient_arrival',
                'final_emergency_time',
                'address_street',
                'address_extra',
                'address_zip_code',
                'address_county',
                'address_col',
                'address_between',
                'address_and_street',
                'address_ref',
                'address_front',
                'address_instructions',
                'address_notes',
                'caller_name',
                'caller_relation',
                'patient_name',
                'patient_gender',
                'patient_age',
                'patient_allergies',
                'patient_illnesses',
                'patient_notes',
                'attention_final_grade',
                'attention_justification',
                'main_complaint',
                'complaint_descriprion',
                'subscription_type'
                ]
    success_url = '/emergency/list/'


class EmergencyClientOdoo(View):
    template_name = "emergency/odooclient.html"
    def get(self, request, *args, **kwargs):
        form = OdooClientForm

        return render(request, self.template_name,{"form": form})

    def post(self, request, *args, **kwargs):
        form = OdooClientForm(request.POST)
        if form.is_valid():
            # Ini Odoo api
            _api_odoo = OdooApi()
            # Get Access token
            result = _api_odoo.get_token()
            logger.info('%s (%s)' % ('Access-Token',result['access_token']))
            if form.cleaned_data['search_type'] == '1':
                patient = form.cleaned_data['client_name']
                patient_data = _api_odoo.get_by_patient_name( patient,result['access_token'])
                #print(patient_data)
                logger.info('%s (%s)' % ('OdooApi',patient_data))
            if form.cleaned_data['search_type'] == '3':
                patient = form.cleaned_data['client_name']
                patient_data = _api_odoo.get_by_patient_id( patient,result['access_token'])
                #print(patient_data)
                logger.info('%s (%s)' % ('OdooApi',patient_data))
            if form.cleaned_data['search_type'] == '2':
                patient = form.cleaned_data['client_name']
                patient_data = _api_odoo.get_by_patient_street( patient,result['access_token'])
                #print(patient_data)
                logger.info('%s (%s)' % ('OdooApi',patient_data))
            if form.cleaned_data['search_type'] == '5':
                patient = form.cleaned_data['client_name']
                patient_data = _api_odoo.get_by_all( patient,result['access_token'])
                #print(patient_data)
                logger.info('%s (%s)' % ('OdooApi',patient_data))
            else:
                return render(request, self.template_name,{"form": form, "result": result})
        return render(request, self.template_name,{"form": form, "result": result, "patients": patient_data})

class EmergencyClientModal(View):
    template_name = "emergency/blank_modal.html"
    def get(self, request, *args, **kwargs):
        form = OdooClientForm
        feContext = {"openmodal":'false',"showMultiple": False,"count": 0}
        find_data = []
        request.session['patientrequest'] = {}
        return render(request, self.template_name,{"form": form, "find_data": find_data, "feContext": feContext})

    def post(self, request, *args, **kwargs):
        form = OdooClientForm(request.POST)
        find_data = []
        patient_data = {}
        feContext = {"openmodal":'true',"showMultiple": True,"count": 0}
        if form.is_valid():
            # Ini Odoo api
            _api_odoo = OdooApi()
            # Get Access token
            result = _api_odoo.get_token()
            logger.info('%s (%s)' % ('OdooApi',result))
            logger.info('%s (%s)' % ('Access-Token',result['access_token']))
            find_data = []

            if form.cleaned_data['search_type'] == '1':
                patient = form.cleaned_data['client_name']
                patient_data = _api_odoo.get_by_patient_name( patient,result['access_token'])
                find_data = patient_data['results']
                feContext.update({"count": len(patient_data['results'])})
                logger.info('%s (%s)' % ('OdooApi_name',patient_data))
            if form.cleaned_data['search_type'] == '2':
                patient = form.cleaned_data['client_name']
                patient_data = _api_odoo.get_by_patient_street( patient,result['access_token'])
                find_data = patient_data['results']
                feContext.update({"count": len(patient_data['results'])})
                logger.info('%s (%s)' % ('OdooApi_street',patient_data))
            if form.cleaned_data['search_type'] == '3':
                patient = form.cleaned_data['client_name']
                patient_data = _api_odoo.get_by_patient_id( patient,result['access_token'])
                find_data = patient_data
                try:
                    if find_data.name:
                        feContext.update({"count": 1})
                except:
                    feContext.update({"count": 0})
                feContext.update({"showMultiple": False})
                logger.info('%s (%s)' % ('OdooApi_id',patient_data))
            if form.cleaned_data['search_type'] == '5':
                patient = form.cleaned_data['client_name']
                patient_data = _api_odoo.get_by_all( patient,result['access_token'])
                find_data = patient_data['results']
                feContext.update({"count": len(patient_data['results'])})
                logger.info('%s (%s)' % ('OdooApi',patient_data))
            if form.cleaned_data['search_type'] == '6':
                patient = form.cleaned_data['client_name']
                patient_data = _api_odoo.get_by_family_member( patient,result['access_token'])
                find_data = patient_data['results']
                feContext.update({"count": len(patient_data['results'])})
                logger.info('%s (%s)' % ('OdooApi_name_family_member',patient_data))
            if form.cleaned_data['search_type'] == '7':
                patient = form.cleaned_data['client_name']
                patient_data = _api_odoo.get_by_company_member( patient,result['access_token'])
                find_data = patient_data['results']
                feContext.update({"count": len(patient_data['results'])})
                logger.info('%s (%s)' % ('OdooApi_name_company_member',patient_data))
            else:
                return render(request, self.template_name,{"form": form, "result": result, "find_data": find_data, "feContext": feContext  })
        return render(request, self.template_name,{'form': form, 'result': result,"find_data": find_data, "feContext": feContext })

class EmergencyNewModal(CreateView):
    template_name = "emergency/blanknew_modal.html"
    model = Emergency
    fields = ['id','odoo_client',
                'service_category',
                'grade_type',
                'zone',
                'start_time',
                'end_time',
                'is_active',
                'unit',
                'unit_assigned_time',
                'unit_dispatched_time',
                'arrival_time',
                'attention_time',
                'derivation_time',
                'hospital_arrival',
                'patient_arrival',
                'final_emergency_time',
                'address_street',
                'address_extra',
                'address_zip_code',
                'address_county',
                'address_col',
                'address_between',
                'address_and_street',
                'address_ref',
                'address_front',
                'address_instructions',
                'address_notes',
                'caller_name',
                'caller_relation',
                'patient_name',
                'patient_gender',
                'patient_age',
                'patient_allergies',
                'patient_illnesses',
                'patient_notes',
                'attention_final_grade',
                'attention_justification',
                'main_complaint',
                'complaint_descriprion',
                'subscription_type'
                ]

    success_url = '/emergency/list/'



class EmergencyGetPatient(View):
    def get(self, request, *args, **kwargs):
        # Read parameter
        target_id = kwargs['patient_id']
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

        logger.info('%s (%s)' % ('OdooApi_patient_data',patient_data))
        logger.info('%s (%s)' % ('OdooApi_parent_data',parent_data))
        request.session['patientrequest'] = patient_json(source_id,patient_data,parent_data)
        return redirect('/emergency/newmodal/')

# Resume and clean patient and partner data
def patient_json(source_id,patient_data,parent_data):
    patient_data_json = {}
    if source_id == 1:
        patient_data_json = {
            "id_odoo_client":  str(patient_data['client_export_id']) + '-' + str(patient_data['id']) + '-' + str(patient_data['id']),
            "id_patient_name":  patient_data['name'],
            "id_patient_allergies" : '',
            "id_patient_illnesses" : '',
            "id_caller_relation": '',
            "id_patient_age": 0,
            "id_zone": patient_data['zone'].upper(),
            "id_subscription_type": patient_data['client_type'],
            "addresses": address_json(patient_data,patient_data),
            "min_addresses": min_address_json(patient_data,patient_data),
        }
    else:
        patient_data_json ={
            "id_odoo_client":  str(parent_data['client_export_id']) + '-' + str(patient_data['parent_id']['id']) + '-' + str(patient_data['id']),
            "id_patient_name":  patient_data['name'],
            "id_patient_allergies" : patient_data['allergies'],
            "id_patient_illnesses" : patient_data['prev_ailments'],
            "id_caller_relation" : partner_relationship(source_id,patient_data['relationship']),
            "id_patient_age": patient_age(patient_data['birthday']),
            "id_zone": parent_data['zone'].upper(),
            "id_subscription_type": parent_data['client_type'],
            "addresses": address_json(parent_data,patient_data),
            "min_addresses": min_address_json(parent_data,patient_data),
        }
    logger.info('%s (%s)' % ('PatientJSON',patient_data_json))
    return patient_data_json

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
    logger.info('%s (%s)' % ('AddressJSON',data))
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
    #data = json.dumps(adress_list)
    data = adress_list
    logger.info('%s (%s)' % ('MinAddressJSON',data))
    return data

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

class EmergencyEnd(View):
    def get(self, request, *args, **kwargs):
        patient_id = kwargs['patient_id']
        try:
            emergency = Emergency.objects.get(id=patient_id)
        except:
            return redirect('/emergency/dashboard/')
        emergency.is_active = False
        emergency.final_emergency_time = datetime.date.today()
        emergency.save()
        return redirect('/emergency/dashboard/')

class OdooSubscription(View):
    template_name = "emergency/search_odoo_auto.html"
    def get(self, request, *args, **kwargs):
        form = OdooClientAuto
        return render(request, self.template_name,{"form": form})

