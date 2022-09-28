# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
# Django
from django.conf import settings
# Python general
from django.template.loader import get_template
from django.template import Context , Template
from django.http import HttpResponse
from django.shortcuts import redirect
# Messages
from django.contrib import messages
# Latex specific
from subprocess import Popen, PIPE
#import tempfile
#from backports import tempfile
import tempfile
import os
import ast
import unicodedata
#from petfile.views import get_petfile_json
from django.conf import settings
import os.path

from paperless.dict_fields import MedicalReportDict
from paperless.models import MedicalReport
from emergency.models import Emergency
# Logging library
import logging
logger = logging.getLogger('django_info')

import base64


# Create your views here.
# generate pdf for screen
def document_as_pdf(request,pk):
  # Get document data
  user = request.user
  params = get_medical_report(pk)

  print(params)
  # Generate QR Signature
  #generate_qr(signature)
  # Clean params strings
  params = escape_params(params)
  #params['diagnostic'] = (params['diagnostic'][:250]+ '...') if len(params['diagnostic']) > 250 else params['diagnostic']
  # print "***************** diagnostic "
  # print params['diagnostic']
  # print "***************** diagnostic end "
  #print params
  generate_tex(params,'pdf')
  tempdir = settings.BASE_DIR+'/templates/printpdf/'
  tex_file = settings.BASE_DIR+'/templates/printpdf/rendered_template'

  if generate_pdf(tempdir,tex_file):    
    #print("PDF Generated Ok")
    logger.info('[ PRINTPDF! - PDF Generated OK]')
    pdf_file = open(os.path.join(tempdir, 'rendered_template.pdf'), 'rb')
    pdf = pdf_file.read()
    r = HttpResponse(content_type='application/pdf')
    r.write(pdf)
    return r
  else:
    #print("PDF Error!!! ckeck /templates/printpdf/rendered_template.log")
    logger.info('[ PRINTPDF! - PDF Error!!! ckeck /templates/printpdf/rendered_template.log]') 
    messages.error(request, "PDF Error!!! ckeck /templates/printpdf/rendered_template.log")
    return redirect('/paperless/')

def document_as_new_pdf(request,pk):
  # Get document data
  user = request.user
  params = get_medical_report(pk)

  print(params)
  # Generate QR Signature
  #generate_qr(signature)
  # Clean params strings
  params = escape_params(params)
  #params['diagnostic'] = (params['diagnostic'][:250]+ '...') if len(params['diagnostic']) > 250 else params['diagnostic']
  # print "***************** diagnostic "
  # print params['diagnostic']
  # print "***************** diagnostic end "
  #print params
  generate_tex(params,'pdf')
  tempdir = settings.BASE_DIR+'/templates/printpdf/'
  tex_file = settings.BASE_DIR+'/templates/printpdf/rendered_template'

  if generate_pdf(tempdir,tex_file):    
    #print("PDF Generated Ok")
    logger.info('[ PRINTPDF! - PDF Generated OK]')
    pdf_file = open(os.path.join(tempdir, 'rendered_template.pdf'), 'rb')
    pdf = pdf_file.read()
    #r = HttpResponse(content_type='application/pdf')
    #r.write(pdf)
    return pdf
  else:
    #print("PDF Error!!! ckeck /templates/printpdf/rendered_template.log")
    logger.info('[ PRINTPDF! - PDF Error!!! ckeck /templates/printpdf/rendered_template.log]') 
    messages.error(request, "PDF Error!!! ckeck /templates/printpdf/rendered_template.log")
    return redirect('/paperless/')


def document_as_pdf_print(request,pk):
  # Get document data
  user = request.user
  #params = get_petfile_json(request, pk)
  print(params)
  # Generate QR Signature
  #generate_qr(signature)
  # Clean params strings
  params = escape_params(params)
  #params['diagnostic'] = (params['diagnostic'][:250]+ '...') if len(params['diagnostic']) > 250 else params['diagnostic']
  # print "***************** diagnostic "
  # print params['diagnostic']
  # print "***************** diagnostic end "
  #print params
  generate_tex(params,'print')
  tempdir = settings.BASE_DIR+'/templates/printpdf/'
  tex_file = settings.BASE_DIR+'/templates/printpdf/rendered_template'

  if generate_pdf(tempdir,tex_file):    
    print("PDF Generated Ok")
    pdf_file = open(os.path.join(tempdir, 'rendered_template.pdf'), 'rb')
    pdf = pdf_file.read()
    r = HttpResponse(content_type='application/pdf')
    r.write(pdf)
    return r
  else:
    #print("PDF Error!!! ckeck /templates/printpdf/rendered_template.log" )
    logger.info('[ PRINTPDF! - PDF Error!!! ckeck /templates/printpdf/rendered_template.log]') 
    messages.error(request, "PDF Error!!! ckeck /templates/printpdf/rendered_template.log")
    return redirect('/petfile/review/')




def generate_medication_tex(params):
  rows = params['petfile_medications']
  #print "******** medications"
  row_tex = ""
  for row in rows:
    #print row
    row_tex +=  '\\item \\textbf{' + escape_text(row['medicine']) + '} \\qquad ' + escape_text(row['indication'])
    #print row_tex
  return row_tex  


def generate_tex(params,output_mode):
  # Assign template
  #Takes tex input from the directory templates/printpdf
  #the pdf-background comes from /static/img/printpdf
  latex_hospital_logo = "hospital_logo.jpg"
  if output_mode == 'pdf':
    #template = get_template('printpdf/petstore_recip_template.tex')
    template = get_template('printpdf/paperless_template.tex')
  else:
    template = get_template('printpdf/paperless_template_print.tex')
  # Define header and footer
  latex_overpic_head = '\\begin{overpic}[width=13.5cm,height=7cm,unit=1mm]{'+ settings.BASE_DIR +'/templates/printpdf/transparent_head.png}'
  latex_overpic_foot = '\\begin{overpic}[width=13.5cm,height=5cm,unit=1mm]{'+ settings.BASE_DIR +'/templates/printpdf/transparent_foot.png}'
  latex_graphics_path = '\\graphicspath{ {'+ settings.BASE_DIR +'/static/img/printpdf/} }'
  #medications_tex = generate_medication_tex(params)
  # Generate context
  context = {
           'content': params,
           #'latex_image_path_local': latex_image_path_local,
           #'all_medications': params["petfile_medications"],
           #'all_medications': medications_tex,
           'latex_hospital_logo':latex_hospital_logo,
           'latex_overpic_head':latex_overpic_head,
           'latex_overpic_foot':latex_overpic_foot,
           'latex_graphics_path':latex_graphics_path,
       }
  #logger.info('[ PRINTPDF! - context {}]'.format(context)) 
  # Render template
  rendered_tpl = template.render(context).encode('utf-8')
  # Write Template to file
  try:
    tex_file = open(settings.BASE_DIR+'/templates/printpdf/rendered_template.tex','wb')
    tex_file.write(rendered_tpl)
    tex_file.close()
    logger.info('[ PRINTPDF! - generate_tex try OK]'.format(context)) 
    return True
  except Exception as e:
    logger.error('[ PRINTPDF! - generate_tex ERROR]')
    logger.error(e)

    return True
    return False


def escape_params(params):
  escaped_params = {}
  for k,v in params.items():
    #print k, 'Corresponds to ', v
    #if isinstance(v,(str, unicode)):
    if isinstance(v,str):    
      escaped_params[k] = escape_text(v)
    else:
      escaped_params[k] = v 
  #print escaped_params 
  return escaped_params

def generate_qr(signature):
  # Create QR code
  img = qrcode.QRCode(
          version=1,
          error_correction=qrcode.constants.ERROR_CORRECT_L,
          box_size=6,
          border=0,
      )
  img = qrcode.make(params['signature'])
  img.save('media/media/qr_signature.jpg')
  return True

def generate_pdf(tempdir,tex_file):
  # Finally read the generated pdf.
  # Remove pdf , log and tex file if exist
  try:
    os.remove(tex_file+'.pdf')
    os.remove(tex_file+'.aux')
    os.remove(tex_file+'.log')

    #print("Deleted pdf, log and tex file")
    logger.info('[ PRINTPDF! - Deleted pdf, log and tex file]')
  except:
    #print("pdf, log and tex file dont exist!")
    logger.info('[ PRINTPDF! - pdf, log and tex file dont exist!]')
  try:  
    process = Popen(
        ['pdflatex', '-output-directory', tempdir],
        stdin=PIPE,
        stdout=PIPE,
    )
    tex_to_pdf = '{}.tex'.format(tex_file).encode()
    process.communicate(tex_to_pdf)
    logger.info('[ PRINTPDF! - tex to pdf succesfull]')
  except Exception as e:
    logger.error('[ PRINTPDF! - generate_tex ERROR 2]')
    logger.error(e) 

  if os.path.exists(tex_file+'.pdf'):
    return True
  else:
    return False
  #return False 

def clean_text(text):
    """ Method to clean characters """
    text = text.replace("\r", "")
    text = text.replace("\t", "")
    text = unicodedata.normalize('NFKD', text).encode('ascii','ignore')
    # Allowed characters for RegEx function:
    # Lower/Mayus characters (a-z) (A-Z) [ascii encoding]
    # Numbers (0-9)
    # Special (.) (/) (() ()) (-) (=) (@)
    # Blank space
    text = ''.join(char for char in text if (re.match("^[A-Za-z0-9. /\-\(\)\=@]*$", char)))
    text = text.strip()
    text = text.replace("\n", " \\"+ "\\ ")
    return text if len(text) != 0 else "N/A"

def escape_text(s):
    # Convert from python escape text to latex format.
    s = s.replace("\'","\\textquotesingle ")
    s = s.replace("<","\\textless ")
    s = s.replace(">","\\textgreater ")
    s = s.replace(u"&","\\& ")
    s = s.replace("\"","``")
    s = s.replace("%","\\% ")
    s = s.replace("#","\\# ")
    s = s.replace("\n", " \\"+ "\\")
    s = s.replace("\r", " \\"+ "\\")
    s = s.replace("_", "\\textunderscore ")
    s = s.replace("{", "\\{ ")
    s = s.replace("}", "\\} ")

    s = s.strip()
    # If no length, return something useful
    if len(s)==0:
        s="NA"
    return s 




def get_medical_report(pk):
  #medical_Report = MedicalReport.get(id=pk)
  medical_Report = MedicalReport.objects.filter(id=pk).values()[0]
  raw_medical_Report = MedicalReport.objects.get(id=pk)
  emergency = Emergency.objects.get(id=raw_medical_Report.service_code)
  medical_Report['json_physical_exploration'] = list(eval(raw_medical_Report.physical_exploration))
  json_medications = list(eval(raw_medical_Report.medications))
  medical_Report['json_medications'] = json_medications

  medical_Report['json_medications_solution'] = group_medications(json_medications,"Hemoderivado-Solucion")
  medical_Report['json_medications_hemder'] = group_medications(json_medications,"Hemoderivado-Hemoderivado")

  medical_Report['json_medications_desfib'] = group_medications(json_medications,"Cardiovascular-Desfibrilacion")
  medical_Report['json_medications_cardio'] = group_medications(json_medications,"Cardiovascular-Cardioversion")

  medical_Report['json_medications_farma'] = group_medications(json_medications,"Farmacologico-Farmaco")
  medical_Report['json_medications_amina'] = group_medications(json_medications,"Farmacologico-Aminas")

  medical_Report['json_airway'] = list(eval(raw_medical_Report.airway)) 
  medical_Report['json_consultation_reason'] = list(eval(raw_medical_Report.consultation_reason))
  medical_Report['json_pupil_state_left'] = list(eval(raw_medical_Report.pupil_state_left))
  medical_Report['json_pupil_state_right'] = list(eval(raw_medical_Report.pupil_state_right))
  medical_Report['json_traumatics'] = list(eval(raw_medical_Report.traumatics))    
  medical_Report['json_inmovilization_type'] = list(eval(raw_medical_Report.inmovilization_type))
  medical_Report['fix_treatment'] = add_line_breaks(raw_medical_Report.treatment,49)
  medical_Report['fix_diagnostic_impresion'] = add_line_breaks(raw_medical_Report.diagnostic_impresion,38)
  medical_Report['fix_current_condition'] = add_line_breaks(raw_medical_Report.current_condition,85)  
  medical_Report['have_client_signature'] = save_png('client_signature',raw_medical_Report.signature_client)
  medical_Report['have_medic_signature'] = save_png('signature_medic',raw_medical_Report.signature_medic)
  medical_Report['emergency_created_at'] = emergency.created_at.strftime('%Y-%m-%d')
  medical_Report['unit_dispatched_time'] = emergency.unit_dispatched_time.strftime('%H:%M')
  medical_Report['arrival_time'] = emergency.arrival_time.strftime('%H:%M')
  medical_Report['attention_time'] = emergency.attention_time.strftime('%H:%M')
  medical_Report['final_emergency_time'] = emergency.final_emergency_time.strftime('%H:%M')
  medical_Report['attention_final_grade'] = str(emergency.attention_final_grade).strip()
  #medical_Report['fix']
  return medical_Report

def group_medications(input_data,filter):
  l = []
  logger.info('[ PRINTPDF! - group medications input_data-------------- {}]'.format(input_data))
  for item in input_data:
    d = {}
    if item["medication_type"] == filter:
      d["medication_name"] = item["medication_name"]
      d["medication_dose"] = item["medication_dose"]
      d["medication_hrs"] = item["medication_hrs"]
      l.append(d)
  logger.info('[ PRINTPDF! - group medications output_data-------------- {}]'.format(l))
  return l

def save_png(target_file,data_uri):
  have_signature_file = True
  if data_uri:
    encoded_data = data_uri.split(",")
    encoded_image = encoded_data[1]
    res = bytes(encoded_image, 'utf-8')
    logger.info('[ PRINTPDF! - signature to png encode -------------- ]')
    png_recovered = base64.decodestring(res)
    logger.info('[ PRINTPDF! - signature to png process {}]'.format(encoded_image))  
    try:
      f = open(settings.BASE_DIR+'/templates/printpdf/{}.png'.format(target_file),'wb')
      f.write(png_recovered)
      f.close
      logger.info('[ PRINTPDF! - signature to png succesfull]')

    except Exception as e:
      logger.error('[ PRINTPDF! - signature ERROR]')
      logger.error(e)
      have_signature_file = False
  else:
    have_signature_file = False
  return have_signature_file

  #decoded_image = Base64.decode64(encoded_image)
  #File.open("signature.png", "wb") { |f| f.write(decoded_image) }



def add_line_breaks(break_string,every):
  #res = '\n '.join(a + b for a, b in zip(break_string[::3], break_string[1::3]))
  #return res
  # initializing K
  K = '\n'
 
  # initializing N
  N = every
 
  x=list(break_string)
  ns=""
  for i in range(0,len(x)):
    if(i!=0 and i%N==0):
        ns+=K
    else:
        ns+=break_string[i]
  return ns
