# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class BaseReport(View):
    template_name = "reports/basereport.html"
    def get(self, request, *args, **kwargs):
        #form = OdooClientForm

        return render(request, self.template_name,{"form": ""})