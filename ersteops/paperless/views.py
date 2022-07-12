from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, ListView
from .models import MedicalReport
from django.utils import timezone
from django.contrib import messages
# Create your views here.
from django.conf import settings
from .forms import MedicalReportForm
from emergency.models import Emergency
from unit.models import CrewMember
from .models import MedicalReport
from unit.models import TodayUnitDoctor
from django.contrib.auth.models import User

from datetime import datetime, timedelta, time
# Logging library
import logging
# Load Logging definition, this is defined in settings.py in the LOGGING section
logger = logging.getLogger('django_info')
from emergency.templatetags import user_tags

from .dict_fields import MedicalReportDict

from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse
import json
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
        'pl_erste_id': qs.erste_code,
        'pl_tel_local': qs.tel_local,
        }
    MedicalReportDict["service_code"] = pl_emergency_id
    MedicalReportDict["service_unit"] = attend_units
    MedicalReportDict["erste_code"] = qs.erste_code
    MedicalReportDict["patient_name"] = qs.patient_name
    MedicalReportDict["patient_age"] = qs.patient_age
    MedicalReportDict["patient_phone"] = qs.tel_local
    MedicalReportDict["patient_address"] = qs.address_street
    MedicalReportDict["geo_key"]= settings.GEO_API_KEY
    MedicalReportDict["copago_amount"] = qs.copago_amount

    request.session['pl_emergency_id'] = pl_emergency_id
    return render(request, self.template_name,{"data": MedicalReportDict,"form":form, })

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

  def get_queryset(self):
    current_user = self.request.user
    
    if user_tags.has_group(current_user,"MedicalReports") and not user_tags.has_group(current_user,"Operator"):
      qs = MedicalReport.objects.filter(user = current_user)
    elif user_tags.has_group(current_user,"Operator"):
      qs = MedicalReport.objects.all()

    return qs


class MedicalReportActive(ListView):
  template_name = "paperless/list_active_medical_reports.html"
  model = Emergency

  def get_queryset(self):
    current_user = self.request.user
    #actual_user = CrewMember.objects.get( user= current_user)
    #actual_date = []
    #actual_date.append(datetime.now().date())
    #actual_date = datetime.now().date() 
    #qs_actual_unit = TodayUnitDoctor.objects.filter(unit_date__gte=actual_date)

    #print("Actual units: {}".format(qs_actual_unit))
    qs = Emergency.objects.filter(is_active = True)
    #qs.filter(units is not null)
    emergency_list = []
    for emergency in qs:
      if emergency.units.count() >0:
        if not emergency.medical_report:
          emergency_list.append(emergency.id)

    qs = Emergency.objects.filter(id__in= emergency_list)
    #qs.filter(medical_report__isnull= True)

    logger.info('[ QS MedicalReportActive! Current User: {} ]'.format(current_user))
    logger.info('[ QS MedicalReportActive! Emegrencies with units: {} ]'.format(emergency_list))
    #logger.info('[ QS MedicalReportActive! Actual Units;: {} ]'.format(qs_actual_unit))
    return qs

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



# Update Timer Functionality
#@csrf_exempt
@csrf_protect
def new_medicalreport(request):
    ''' '''
    bad_response = JsonResponse({'status':'bad request'})
    bad_response.status_code = 400
    current_user = request.user
    if not request.is_ajax():
        logger.info('[ NEW MEWDICAL REPORT -1- Not ajax: {} ]'.format(current_user))
        logger.info('[ NEW MEWDICAL REPORT DATA: {} ]'.format(data))
        return bad_response
    if not request.body:
        logger.info('[ NEW MEWDICAL REPORT -2- Not body: {} ]'.format(current_user))
        logger.info('[ NEW MEWDICAL REPORT DATA: {} ]'.format(data))
        return bad_response

    data = json.loads(request.body.decode('utf-8'))

    #logger.info('[ NEW MEWDICAL REPORT: -3- {} ]'.format(current_user))
    #logger.info('[ NEW MEWDICAL REPORT DATA: -4- {} ]'.format(data))
    #if 'id' in data and 'timer_type' in data :
    if 'paperless' in data :
      #qs =  Emergency.objects.get(pk = pl_emergency_id)
      try:
          logger.info('[ NEW MEWDICAL REPORT DATA: -5- {} ]'.format(data['paperless']))
          vue_data=json.loads(data['paperless'])
          logger.info('[ NEW MEWDICAL REPORT DATA: -6- {} ]'.format(vue_data['service_code']))
          qs = Emergency.objects.get(id=vue_data['service_code'])
          medicalReport = MedicalReport.objects.create(
          odoo_client = qs.odoo_client,
          erste_code = qs.erste_code,
          service_code = vue_data['service_code'],
          service_geo_lat = vue_data['service_geo_lat'],
          service_geo_lon = vue_data['service_geo_lon'],
          service_unit = vue_data['service_unit'],  
          service_unit_type = vue_data['service_unit_type'],
          service_unit_plate = vue_data['service_unit_plate'],
          patient_name = vue_data['patient_name'],
          patient_gender = vue_data['patient_gender'],
          patient_age = vue_data['patient_age'],
          patient_affiliations = vue_data['patient_affiliations'],
          is_patient_unknow = vue_data['is_patient_unknow'], 
          patient_unknow = vue_data['patient_unknow'],
          patient_clothes = vue_data['patient_clothes'],
          copago_amount = vue_data['copago_amount'],
          skin_color = vue_data['skin_color'],
          attention_place = vue_data['attention_place'],
          other_attention_place = vue_data['other_attention_place'],
          consultation_reason = vue_data['consultation_reason'],
          other_consultation_reason = vue_data['other_consultation_reason'],

          user = request.user,
          )
          messages.error(request, "Parte Medico Guardado correctamente!!!")
          # if data['timer_type'] == '1':
          #     emergency.unit_dispatched_time = timezone.now()
          # if data['timer_type'] == '2':
          #     emergency.arrival_time = timezone.now()
          #     emergency.attention_time = timezone.now()
          # if data['timer_type'] == '3':
          #     emergency.derivation_time = timezone.now()
          # if data['timer_type'] == '4':
          #     emergency.patient_arrival = timezone.now()

          # emergency.save()
          data.update({'status': 'success', 'client_id':emergency.odoo_client})
          response = JsonResponse(data)
          response.status_code = 202
          return response
      except Exception as e:
          logger.error("[Create Medical Report View ERROR]: {}, type: {}".format(e, type(e)))
          return bad_response
      qs.medical_report = medicalReport
      qs.save()

    else:
        return bad_response
# /Update Timer Functionality