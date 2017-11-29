# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import View, CreateView, ListView
from emergency.models import Emergency
from django.utils import timezone


class EmergencyBlank(View):
	template_name = "emergency/blank.html"
	def get(self, request, *args, **kwargs):
		form=''
		return render(request, self.template_name,{"form": form})



class EmergencyNew(CreateView):
	template_name = "emergency/new.html"
	model = Emergency
	fields = ['odoo_client','grade_type','zone','start_time','end_time','is_active','unit']
	success_url = '/emergency/list/'

class EmergencyListView(ListView):
    template_name = "emergency/list.html"
    model = Emergency
    def get_context_data(self, **kwargs):
        context = super(EmergencyListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context