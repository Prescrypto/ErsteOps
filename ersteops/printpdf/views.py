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

# Logging library
import logging
logger = logging.getLogger('django_info')


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
    return redirect('/petfile/review/')

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
  latex_hospital_logo = "hospital_logo.jpg"
  if output_mode == 'pdf':
    template = get_template('printpdf/petstore_recip_template.tex')
  else:
    template = get_template('printpdf/petstore_recip_template_print.tex')
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
  logger.info('[ PRINTPDF! - context {}]'.format(context)) 
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
  

  return medical_Report


