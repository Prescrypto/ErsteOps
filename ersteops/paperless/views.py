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
from django.core.mail import EmailMessage
import os.path
from printpdf.views import document_as_new_pdf

from django.core.files.base import ContentFile, File

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
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



@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
class MedicalReportDetail(View):
  template_name = "paperless/detail_medical_report_2.html"

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
    # Save data from FE to MODEL
    if 'paperless' in data :
      #qs =  Emergency.objects.get(pk = pl_emergency_id)
      try:
          logger.info('[ NEW MEWDICAL REPORT DATA: -5- {} ]'.format(data['paperless']))
          vue_data=json.loads(data['paperless'])
          logger.info('[ NEW MEWDICAL REPORT DATA: -6- {} ]'.format(vue_data['service_code']))
          #logger.info('[ NEW MEWDICAL REPORT DATA: -7- {} ]'.format(vue_data['signature_client']))
          qs = Emergency.objects.get(id=vue_data['service_code'])
          medicalReport = MedicalReport.objects.create(
          odoo_client = qs.odoo_client,
          erste_code = qs.erste_code,
          service_code = vue_data['service_code'],
          service_unit= vue_data['service_unit'], 
          service_unit_type= vue_data['service_unit_type'], 
          service_unit_plate= vue_data['service_unit_plate'], 
          service_geo_lat= vue_data['service_geo_lat'], 
          service_geo_lon= vue_data['service_geo_lon'], 
          patient_name= vue_data['patient_name'], 
          patient_gender= vue_data['patient_gender'], 
          patient_age= vue_data['patient_age'], 
          patient_affiliations= vue_data['patient_affiliations'],
          is_patient_unknow= vue_data['is_patient_unknow'], 
          patient_unknow= vue_data['patient_unknow'], 
          patient_clothes= vue_data['patient_clothes'], 
          patient_phone= vue_data['patient_phone'],
          patient_address= vue_data['patient_address'], 
          copago_amount= vue_data['copago_amount'],
          attention_place= vue_data['attention_place'],
          other_attention_place= vue_data['other_attention_place'], 
          skin_color= vue_data['skin_color'], 
          service_type= vue_data['service_type'], 
          other_service_type= vue_data['other_service_type'],
          consultation_reason= vue_data['consultation_reason'],
          other_consultation_reason= vue_data['other_consultation_reason'], 
          event_type= vue_data['event_type'], 
          traumatics= vue_data['traumatics'],
          other_traumatics= vue_data['other_traumatics'], 
          airway= vue_data['airway'],
          other_airway= vue_data['other_airway'], 
          physical_exploration= vue_data['physical_exploration'], 
          normal_head= not_find_on_list(vue_data['normal_elements'],'Cabeza'), 
          normal_face= not_find_on_list(vue_data['normal_elements'],'Cara'), 
          normal_neck= not_find_on_list(vue_data['normal_elements'],'Cuello'), 
          normal_torax= not_find_on_list(vue_data['normal_elements'],'Tórax'), 
          normal_abdomen= not_find_on_list(vue_data['normal_elements'],'Abdomen'), 
          normal_limbs= not_find_on_list(vue_data['normal_elements'],'Extremidades'), 
          normal_genitals= not_find_on_list(vue_data['normal_elements'],'Genitales'), 
          normal_spine= not_find_on_list(vue_data['normal_elements'],'Columna Vertebral'), 
          current_condition= vue_data['current_condition'], 
          pupil_state_left= vue_data['pupil_state_left'], 
          pupil_state_right= vue_data['pupil_state_right'], 
          pathological_history_daibetes_melitus= find_on_list(vue_data['pathological_history'],'Diabetes Melitus'),
          pathological_history_arterial_hypertension= find_on_list(vue_data['pathological_history'],'Hipertension Arterial'),
          pathological_history_heart_disease= find_on_list(vue_data['pathological_history'],'Cardiopatias'),
          pathological_history_pneumopathies= find_on_list(vue_data['pathological_history'],'Neumopatias'),
          pathological_history_trauma= find_on_list(vue_data['pathological_history'],'Quirurgicos'),
          pathological_history_alergy= find_on_list(vue_data['pathological_history'],'Alergias'),
          other_pathological_history = vue_data['other_pathological_history'], 
          current_therapeutics= vue_data['current_therapeutics'], 
          description_of_injuries= vue_data['description_of_injuries'], 
          diagnostic_impresion= vue_data['diagnostic_impresion'],
          treatment= vue_data['treatment'], 
          derivation= vue_data['derivation'], 
          derivation_place= vue_data['derivation_place'], 
          state_of_health= vue_data['state_of_health'],
          demarcation= vue_data['demarcation'],
          crum = vue_data['crum'],
          crum_reception = vue_data['crum_reception'],
          medications = vue_data['medications'],
          inmovilization = vue_data['inmovilization'],
          inmovilization_type = vue_data['inmovilization_type'],
          other_inmovilization_type = vue_data['other_inmovilization_type'],
          electro_rhythm= vue_data['electro_rhythm'],
          electro_frequency= vue_data['electro_frequency'],
          electro_wave_p= vue_data['electro_wave_p'],
          electro_pr= vue_data['electro_pr'],
          electro_axis_qrs= vue_data['electro_axis_qrs'],
          electro_st= vue_data['electro_st'],
          electro_wave_t= vue_data['electro_wave_t'],
          electro_qt= vue_data['electro_qt'],
          electro_abnormalities= vue_data['electro_abnormalities'],
          electro_interpretation= vue_data['electro_interpretation'],
          derivation_amount= vue_data['derivation_amount'],
          derivation_recive= vue_data['derivation_recive'],
          derivation_type= vue_data['derivation_type'],
          demarcation_responsable = vue_data['demarcation_responsable'],
          demarcation_relation = vue_data['demarcation_relation'],
          user = request.user,
          electro_qrs = vue_data['electro_qrs'],
          email = vue_data['email'],
          send_email = vue_data['send_email'],
          derivation_hospital = vue_data['derivation_hospital'],
          crum_hospital = vue_data['crum_hospital'],
          crum_notes = vue_data['crum_notes'],
          notes = vue_data['notes'],
          detail_pat_history_daibetes_melitus = vue_data['detail_pat_history_daibetes_melitus'],
          detail_pat_history_arterial_hypertension = vue_data['detail_pat_history_arterial_hypertension'],
          detail_pat_history_heart_disease = vue_data['detail_pat_history_heart_disease'],
          detail_pat_history_pneumopathies = vue_data['detail_pat_history_pneumopathies'],
          detail_pat_history_trauma = vue_data['detail_pat_history_trauma'],
          detail_pat_history_alergy = vue_data['detail_pat_history_alergy'],
          det_normal_head = vue_data['det_normal_head'],
          det_normal_face = vue_data['det_normal_face'],
          det_normal_neck = vue_data['det_normal_neck'],          
          det_normal_torax = vue_data['det_normal_torax'],
          det_normal_abdomen = vue_data['det_normal_abdomen'],
          det_normal_limbs = vue_data['det_normal_limbs'],
          det_normal_genitals = vue_data['det_normal_genitals'],
          det_normal_spine = vue_data['det_normal_spine'],
          crew_medic = vue_data['crew_medic'],
          crew_medic_id_card = vue_data['crew_medic_id_card'],
          crew_tum = vue_data['crew_tum'],
          crew_operator = vue_data['crew_operator'],
          signature_client = vue_data['signature_client'],
          signature_medic = vue_data['signature_medic'],
          odoo_client_name = qs.partner_name,
          )
          messages.info(request, "Parte Medico Guardado correctamente!!!")
          messages.info(request, "Parte Medico Generating pdf!!!")
          #pdf_to_attach = settings.BASE_DIR+'/templates/printpdf/rendered_template.pdf/'
          tempdir = settings.BASE_DIR+'/templates/printpdf/'
          pdf = document_as_new_pdf(request,medicalReport.id)

          if pdf:
            tempdir = settings.BASE_DIR+'/templates/printpdf/'
            pdf_file = open(os.path.join(tempdir, 'rendered_template.pdf'), 'rb')
            pdf = pdf_file.read()
            messages.info(request, "Parte Medico Sending email with pdf!!!")
            Send_Mail_To(request,vue_data['email'],medicalReport.id,vue_data['send_email'],pdf)
            d = medicalReport.created_at.strftime('%Y-%m-%d')
            file_name = 'Parte_Medico_Vida_Uno_{}_{}.pdf'.format(d,str(medicalReport.id))
            medicalReport.email_sent = True
            medicalReport.save()
            medicalReport.final_report.save(file_name,ContentFile(pdf))
            #medicalReport.save()
            # emergency.save()
          data.update({'status': 'success', 'client_id':qs.odoo_client})
          response = JsonResponse(data)
          response.status_code = 202
          return response
      except Exception as e:
          medicalReport.email_sent = False
          medicalReport.save()
          logger.error("[Create Medical Report View ERROR SENDING EMAIL]: {}, type: {}".format(e, type(e)))
          #return bad_response
          return redirect('/paperless')

      #qs.medical_report = medicalReport
      #qs.save()

    else:
        return bad_response
# /Update Timer Functionality

def find_on_list(my_list_Dict, what_to_search):
  #define Yes or No if key is on dict
  my_text='No'
  if my_list_Dict.count(what_to_search) > 0:
    my_text = 'Si'
  return my_text

def not_find_on_list(my_list_Dict, what_to_search):
  #define Yes or No if key is on dict
  my_text='Si'
  if my_list_Dict.count(what_to_search) > 0:
    my_text = 'No'
  return my_text


def Send_Mail_To(request,email_recive,pk,send_flag,pdf):
  #Send mail via smtp gmail server
  #pdf_to_attach = settings.BASE_DIR+'/templates/printpdf/rendered_template.pdf/'
  #tempdir = settings.BASE_DIR+'/templates/printpdf/'
  #pdf = document_as_new_pdf(request,pk)
  # Test if pdf was generated correctly
  #try:
  #  pdf_file = open(os.path.join(tempdir, 'rendered_template.pdf'), 'rb')
  #except Exception as e:
  #  send_flag = False
  #  logger.error("[Create Medical Report Email ERROR not pdf]: {}, type: {}".format(e, type(e)))
  #  return bad_response
  try:
    email = EmailMessage(
      'Parte Medico Vida uno Folio {}'.format(pk),
      'Ha recibido su parte médico digital del emisor EMERGENCIAS MEDICAS DE MEDICO SC con Folio:{}'.format(pk),
      'info@keepitsimple.com.mx',
      [ email_recive, ]
    )    
    file_name = 'Parte_Medico_Vida_Uno_{}.pdf'.format(str(pk))
    email.attach(file_name,pdf,'application/pdf')
    #pdf_to_attach = os.path.join(tempdir, 'rendered_template.pdf')
    #email.attach_file(pdf_to_attach)
    if send_flag:
      email.send()
    logger.info('[ NEW MEWDICAL SendMail : {} ]'.format(email_recive))
  except Exception as e:
    logger.error("[Create Medical Report Email ERROR]: {}, type: {}".format(e, type(e)))
    return bad_response

