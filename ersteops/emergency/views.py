# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import View, CreateView, ListView

class EmergencyRecord(View):
	template_name= "emergency/blank.html"
	def get(self, request, *args, **kwargs):
		form=''
		return render(request, self.template_name,{"form": form})
