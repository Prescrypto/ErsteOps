from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, ListView
from .models import MedicalReport
from django.utils import timezone
from django.contrib import messages
# Create your views here.
from django.conf import settings
from .forms import MedicalReportForm
from emergency.models import Emergency
from .models import MedicalReport

# Logging library
import logging
# Load Logging definition, this is defined in settings.py in the LOGGING section
logger = logging.getLogger('django_info')

#def emergency_data_dict(emergency):


#@method_decorator(login_required, name='dispatch')
class MedicalReportNew(View):
  template_name = "paperless/new_medical_report_vue.html"
  #model = MedicalReport
  def get(self, request, *args, **kwargs):
    form = MedicalReportForm()
    pl_emergency_id = self.kwargs['pk']
    
    try:
      qs = Emergency.objects.get(pk = pl_emergency_id)
      logger.info('[ GET EMERGENCY FOR FILLUP EMERGENCY FORM SUCCESS: {}]'.format(qs.patient_name))
    except Exception as e:
      logger.error("DEBUG: MedicalReport New")
      logger.error("ERROR FORMATING MESSAGE ERROR! ")
      logger.error(e) 
      content = "Emergencia no encontrada!"
      return redirect('/')
    attend_units=""  
    for unit in qs.units.all():
        attend_units = '{}'.format(unit) 
    data = {
        'geo_key': settings.GEO_API_KEY, 
        'pl_emergency_id': pl_emergency_id,
        'pl_unit': attend_units, 
        'pl_patient_name': qs.patient_name,
        }

    request.session['pl_emergency_id'] = pl_emergency_id
    return render(request, self.template_name,{"data":data,"form":form,})

  def post(self, request, *args, **kwargs):
    form = MedicalReportForm(request.POST)
    data = {'geo_key': settings.GEO_API_KEY, 'pl_emergency_id': request.session['pl_emergency_id']}
    pl_emergency_id = request.session['pl_emergency_id']

    if form.is_valid():
      qs =  Emergency.objects.get(pk = pl_emergency_id)
      if not qs.medical_report:
        try:
          medicalReport = MedicalReport.objects.create(
            odoo_client = qs.odoo_client,
            erste_code = qs.erste_code,
            service_code = request.session['pl_emergency_id'],
            service_geo_lat = form.cleaned_data['service_geo_lat'],
            service_geo_lon = form.cleaned_data['service_geo_lon'],
            service_unit = form.cleaned_data['service_unit'],  
            service_unit_type = form.cleaned_data['service_unit_type'],
            service_unit_plate = form.cleaned_data['service_unit_plate'],
            patient_name = form.cleaned_data['patient_name'],
            patient_gender = form.cleaned_data['patient_gender'],
            patient_age = form.cleaned_data['patient_age'],
            patient_affiliations = form.cleaned_data['patient_affiliations'], 
            patient_unknow = form.cleaned_data['patient_age'],
            patient_clothes = form.cleaned_data['patient_clothes'],
            user = request.user,
            )
          messages.error(request, "Parte Medico Guardado correctamente!!!")
          logger.info('[ POST FILLUP MEDICALREPORT FORM SUCCESS! ]')
        except Exception as e:
          logger.error("[ ERROR: MEDICAL REPORT NEW - POST ]")
          logger.error("[ ERROR: CREATE MEDICAL REPORT ERROR!] ")
          logger.error(e)
          messages.error(request, "Verifica los datos requeridos del parte medico") 
          return render(request, self.template_name,{"form": form,})
        qs.medical_report = medicalReport
        qs.save()


      else:
        logger.error("[ ERROR: MEDICAL REPORT NEW - POST ]")
        logger.error("[ ERROR: MEDICAL REPORT ALREADY EXIST!] ")
        messages.error(request, "Ya existe el parte medico para esa emergencia")
        return redirect('/paperless/')
    else:
      #form invalid
      logger.error("[ ERROR: MEDICAL REPORT NEW - POST ]")
      logger.error("[ ERROR: FORM INVALID CREATE MEDICAL REPORT! ] ")
      messages.error(request, "Verifica los datos requeridos del parte medico")
      #return redirect('/paperless/')
      return render(request, self.template_name,{"form": form,})
    request.session['']
    return redirect('/paperless/')
  # def get_context_data(self, **kwargs):
  #   context = super(MedicalReportNew, self).get_context_data(**kwargs)
  #   #context['emergency_id'] = self.kwargs['pk']

  #   return context



#@method_decorator(login_required, name='dispatch')
class MedicalReportList(ListView):
  #template_name = "paperless/paperless_list.html"
  template_name = "paperless/list_medical_reports.html"
  model = MedicalReport

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['now'] = timezone.now()
    return context


class MedicalReportDetail(View):
  template_name = "paperless/detail_medical_report.html"

  def get(self, request, *args, **kwargs):
    pk_medical_report= self.kwargs['pk']
    try: 
      qs = MedicalReport.objects.get(pk = pk_medical_report)
      messages.error(request, "Parte Medico EXTRAIDO correctamente!!!")
      logger.info('[ GET MEDICAL REPORT INFO SUCCESS! ]')
    except:
      logger.error("[ ERROR: MEDICAL REPORT RETRIVE - POST ]")
      logger.error("[ ERROR: MEDICAL REPORT ALREADY EXIST!] ")
      messages.error(request, "NO EXISTE ESTE PARTE MEDICO {}".format(pk_medical_report))

    return render(request, self.template_name,{"data":qs,})

#   def post (self, request, *args, **kwargs):
#     return redirect('/paperless/')
