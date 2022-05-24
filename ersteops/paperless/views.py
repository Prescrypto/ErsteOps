from django.shortcuts import render
from django.views.generic import View, CreateView, ListView
from .models import MedicalReport
# Create your views here.

class MedicalReportNew(CreateView):
    template_name = "paperless/paperless_new.html"
    model = MedicalReport





class MedicalReportList(ListView):
    #template_name = "paperless/paperless_list.html"
    template_name = "paperless/paperless_map.html"
    model = MedicalReport
