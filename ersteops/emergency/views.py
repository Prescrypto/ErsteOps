# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.views.generic import View, CreateView, ListView, DetailView, UpdateView
from emergency.models import Emergency,AttentionDerivation
from django.utils import timezone
from emergency.forms import OdooClientForm
from core.utils import OdooApi
import requests
from requests.auth import HTTPBasicAuth
import json
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
    fields = ['odoo_client',
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
                'patient_allergies',
                'patient_illnesses',
                'patient_notes',
                'main_complaint',
                'complaint_descriprion',
                'required_attention',
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
        context['now'] = timezone.now()
        return context


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
                'patient_allergies',
                'patient_illnesses',
                'patient_notes',
                'main_complaint',
                'complaint_descriprion',
                'required_attention',
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
    # template_name = "emergency/blank_modal.html"
    # def get(self, request, *args, **kwargs):
    #     form=''
    #     return render(request, self.template_name,{"form": form})
    template_name = "emergency/blank_modal.html"
    def get(self, request, *args, **kwargs):
        form = OdooClientForm
        jq_openmodal = 'false'
        request.session['patientrequest'] = {}
        return render(request, self.template_name,{"form": form, "openmodal": jq_openmodal})

    def post(self, request, *args, **kwargs):
        form = OdooClientForm(request.POST)
        find_data = []
        if form.is_valid():
            jq_openmodal = 'true'
            # Ini Odoo api
            _api_odoo = OdooApi()
            # Get Access token
            result = _api_odoo.get_token()
            logger.info('%s (%s)' % ('OdooApi',result))
            logger.info('%s (%s)' % ('Access-Token',result['access_token']))
            if form.cleaned_data['search_type'] == '1':
                patient = form.cleaned_data['client_name']
                patient_data = _api_odoo.get_by_patient_name( patient,result['access_token'])
                logger.info('%s (%s)' % ('OdooApi',patient_data))
            if form.cleaned_data['search_type'] == '2':
                patient = form.cleaned_data['client_name']
                patient_data = _api_odoo.get_by_patient_street( patient,result['access_token'])
                #print(patient_data)
                find_data = json.dumps(patient_data['results'])
                logger.info('%s (%s)' % ('OdooApi',patient_data))
            if form.cleaned_data['search_type'] == '3':
                patient = form.cleaned_data['client_name']
                patient_data = _api_odoo.get_by_patient_id( patient,result['access_token'])
                #print(patient_data)
                find_data = []
                logger.info('%s (%s)' % ('OdooApi',patient_data))
            if form.cleaned_data['search_type'] == '5':
                patient = form.cleaned_data['client_name']
                patient_data = _api_odoo.get_by_all( patient,result['access_token'])
                #print(patient_data)
                find_data = json.dumps(patient_data['results'])
                logger.info('%s (%s)' % ('OdooApi',patient_data))
            else:
                return render(request, self.template_name,{"form": form, "result": result, "openmodal": jq_openmodal, })
        return render(request, self.template_name,{'form': form, 'result': result, 'patients': patient_data, 'openmodal': jq_openmodal})

class EmergencyNewModal(CreateView):
    template_name = "emergency/blanknew_modal.html"
    model = Emergency
    fields = ['odoo_client',
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
                'patient_allergies',
                'patient_illnesses',
                'patient_notes',
                'main_complaint',
                'complaint_descriprion',
                'required_attention',
                'subscription_type',
                'patient_gender',
                'patient_age',
                ]
    
    success_url = '/emergency/list/'



class EmergencyGetPatient(View):
    def get(self, request, *args, **kwargs):
        patient_id = kwargs['patient_id']
        # Ini Odoo api
        _api_odoo = OdooApi()
        result = _api_odoo.get_token()
        patient_data = _api_odoo.get_by_patient_id( patient_id,result['access_token'])
        request.session['patientrequest'] = patient_data
        return redirect('/emergency/newmodal/')