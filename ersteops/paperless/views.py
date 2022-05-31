from django.shortcuts import render
from django.views.generic import View, CreateView, ListView
from .models import MedicalReport
from django.utils import timezone
# Create your views here.



class MedicalReportNew(ListView):
    template_name = "paperless/paperless_new_medical_report.html"
    model = MedicalReport





class MedicalReportList(ListView):
    #template_name = "paperless/paperless_list.html"
    template_name = "paperless/paperless_list_medical_reports.html"
    model = MedicalReport

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
