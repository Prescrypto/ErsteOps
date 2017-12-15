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
        patient_id = kwargs['patient_id']
        # Ini Odoo api
        _api_odoo = OdooApi()
        result = _api_odoo.get_token()
        patient_data = _api_odoo.get_by_patient_id( patient_id,result['access_token'])
        request.session['patientrequest'] = patient_data
        return redirect('/emergency/newmodal/')


class OdooSubscription(View):
    template_name = "emergency/search_odoo_auto.html"
    def get(self, request, *args, **kwargs):
        form = OdooClientAuto
        return render(request, self.template_name,{"form": form})

