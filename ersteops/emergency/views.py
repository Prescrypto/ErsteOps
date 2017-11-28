# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import View, CreateView, ListView
from emergency.models import Emergency

class EmergencyBlank(View):
	template_name = "emergency/blank.html"
	def get(self, request, *args, **kwargs):
		form=''
		return render(request, self.template_name,{"form": form})



class EmergencyNew(CreateView):
	template_name = "emergency/new.html"
	model = Emergency
	fields = ['odoo_client','grade_type','zone','start_time','end_time','is_active','unit']