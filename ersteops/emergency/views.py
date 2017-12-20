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
#from datetime import datetime, timedelta
import datetime
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


class EmergencyDashbordList(ListView):
    template_name = "emergency/dashbord.html"
    model = Emergency
    def get_context_data(self, **kwargs):
        context = super(EmergencyDashbordList, self).get_context_data(**kwargs)
        context.update({'now': timezone.now()})
        return context

    def get_queryset(self):
        return Emergency.objects.filter(is_active=True)


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
        #request.session['patientrequest'] = patient_data
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
        }
    print("*************** patient_json ***************")
    print(patient_data_json)
    print("********************************************")
    return patient_data_json

def partner_relationship(source_id,patient_relation):
    relationship = ""
    if source_id == 2:
        if patient_relation == "1":
            relationship = "Padre"
        elif patient_relation == "2":
            relationship = "Madre"
        elif patient_relation == "3":
            relationship = "Esposo/a"
        elif patient_relation == "4":
            relationship = "Descendiente"
        elif patient_relation == "5":
            relationship = "Otro Familiar"
        else:
            relationship = "No clasificado"
    elif source_id ==3:
        if patient_relation == "1":
            relationship = "Dueño"
        elif patient_relation == "2":
            relationship = "Director"
        elif patient_relation == "3":
            relationship = "Ejecutivo"
        elif patient_relation == "4":
            relationship = "Administrador"
        elif patient_relation == "5":
            relationship = "Empleado"
        elif patient_relation == "6":
            relationship = "Otro"
        else:
            relationship = "No clasificado"

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
                    "id_address_street": address['street'],
                    "id_address_extra": address['street2'],
                    "id_address_zip_code": '',
                    "id_address_county": address['sat_municipio_id']['nombre_municipio'],
                    "id_address_col": address['sat_colonia_id']['nombre_colonia'],
                }
                adress_list.append(adresses_json)
    if len(adress_list) == 0:
        print("*** por aqui ******")
        adresses_json = {
                    "id_address_street": parent_data['street'],
                    "id_address_extra": parent_data['street2'],
                    "id_address_zip_code": parent_data['zip'],
                    "id_address_county": '',
                    "id_address_col": '',
        }
        adress_list.append(adresses_json)
    data = json.dumps(adress_list)
    print(" **************** parent_data len ****************")
    print(len(parent_data['child_ids']))
    print(" **************** address_list len ****************")
    print(len(adress_list))
    logger.info('%s (%s)' % ('AddressJSON',data))
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

