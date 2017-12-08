# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import View, CreateView, ListView, DetailView, UpdateView
from emergency.models import Emergency,AttentionDerivation
from django.utils import timezone
from emergency.forms import OdooClientForm
from core.utils import OdooApi
import requests
from requests.auth import HTTPBasicAuth

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
        _api_odoo = OdooApi()
        result = _api_odoo.get_token()
        print("*********** access token ***********")
        print(result['access_token'])
        return render(request, self.template_name,{"form": form})



