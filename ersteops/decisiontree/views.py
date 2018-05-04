# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.views.generic import View, CreateView, ListView, DetailView
from .forms import UploadSymptomDataFileForm, SymptomSearchForm
from django.http import HttpResponseRedirect, HttpResponse
# Messages
from django.contrib import messages
# csv
import csv
# open file from url
import urllib3
import unicodedata
from django.utils.encoding import python_2_unicode_compatible
import time
import datetime
from datetime import datetime, date
from .models import SymptomDataDetail,SymptomDataFile,SymptomType

# Create your views here.
class UploadSymptomData(View):
  template_name = "decisiontree/UploadSymptomData.html"
  def get(self, request, *args, **kwargs):
    form = UploadSymptomDataFileForm()
    data = {}
    data['show_progress_bar']=False
    data['show_form']=True
    data['show_buttons']=True
    data['show_final_progress_bar']=False
    return render(request, self.template_name,{"form": form,'data':data})

  def post(self, request, *args, **kwargs):
    form = UploadSymptomDataFileForm(request.POST,request.FILES)
    if form.is_valid():
      form_object = form.save()
      print(form_object.id)
      messages.success(request, "Los datos de sintomas fueron actualizados exitosamente.")
      return HttpResponseRedirect('/decisiontree/upload/'+str(form_object.id)+'/')
    else:
      data = {}
      data['show_buttons']=True
    return render(request, self.template_name,{"form": form,'data':data})

class ProcessUploadSymptomData(View):
  template_name = "decisiontree/UploadSymptomData.html"
  def get(self, request, *args, **kwargs):
    data_id = kwargs['data_id']
    print(data_id)
    #process_employees = ProcessUpdateSymptomEmployees(request.user)
    process_data = ProcessUploadSymptomDataFile(data_id,request.user)
    data = {}
    data['show_buttons']=False
    data['show_final_progress_bar']=True
    data['read_lines'] = process_data['read_lines']
    data['insert_lines'] = process_data['insert_lines']
    data['update_lines'] = process_data['update_lines']
    data['inserted_employees'] = 0 #process_employees['inserted_employees']
    data['existing_employees'] = 0 #process_employees['existing_employees']
    #print process_data
    return render(request, self.template_name,{"data": data,})

# Upsert csv data into table BiometricDataDetail
def ProcessUploadSymptomDataFile(data_id,user):
  data = SymptomDataFile.objects.get(id=data_id)
  print(data.symptom_file.url)
  have_errors = False
  result_error = []
  read_lines = 0
  insert_lines = 0
  update_lines = 0
  error_lines = 0
  print("********* before open file")
  with open(data.symptom_file.url,encoding="latin-1") as csvfile:
    reader = csv.DictReader(csvfile)
    print("********* with open file")
    for idx,row in enumerate(reader):
      print("*********** inside for")
      print (row)
      # Extract ampm and clean 
      #date_ampm = row['Fecha/Hora'][-5:]
      #Date/Time
      #date_ampm = row['Date/Time'][-5:]
      #date_ampm = row['Date/Time']
      #date_ampm = date_ampm.replace('.','')
      #date_ampm = date_ampm.replace(' ','')
      # Extract Date and time
      #date_datetime = row['Fecha/Hora'][:19]
      #date_datetime = row['Date/Time'][:19]
      # Convert to datetime object
      #datetime_object = datetime.strptime(date_datetime+' '+date_ampm,'%d/%m/%Y %I:%M:%S %p')
      #datetime_object = datetime.strptime(date_datetime+' '+date_ampm,'%d/%m/%Y %H:%M:%S')
      #datetime_object = datetime.strptime(date_ampm,'%d/%m/%Y %H:%M:%S')
      #print(datetime_object)
      # Convert date to seconds
      #datetime_object_int = str(time.mktime(datetime_object.timetuple()))
      # obtain final idx
      #datetime_object_idx = row['No.']+'-'+datetime_object_int
      # Get event type
      #sel_event_type = BioEventType.objects.get(event_type_id='atte')
      # Prepare save
      # loademployedata = BiometricDataDetail(
      #     idx = datetime_object_idx,
      #     name = row['Name'].decode('latin-1'),
      #     depto = row['Department'],
      #     employe_id = row['No.'],
      #     location_id = row['Location ID'],
      #     date_rec = datetime_object,
      #     event_type = sel_event_type,
      #     user = user,
      #     )

      sel_symtom_type = SymptomType.objects.get(symptom_id=row['symptom_type'])
      print("********************* ")
      print(">>"+row['symptom_type']+"<<")
      print(row['Sintoma'])
      #print(row['Sintoma'].decode('latin-1'))
      # Prepare save
      loademployedata = SymptomDataDetail(
          idx = row['symptom_id'],
          #name = row['Sintoma'].decode('latin-1'),
          name = row['Sintoma'],
          n1 = row['N1'],
          n2 = row['N2'],
          n3 = row['N3'],
          n4 = row['N4'],
          n5 = row['N1'],
          n6 = row['N2'],
          n7 = row['N3'],
          level = row['Nivel'],
          grade = row['Grado'],
          key = row['Clave'],
          symptom_type = sel_symtom_type,
          )
      # Save to database
      try:
        try:
          loademployedata.save()
          print("******** insert ")
          insert_lines += 1
        except:
          loademployedata.save(update_fields=['name','grade','level','symptom_type'])
          print("******** update")
          update_lines += 1
      except Exception as e :
        data_error = {}
        data_error['exception'] = e
        data_error['linea'] = idx
        result_error.append(data_error)
        have_errors = True
        error_lines += 1

    read_lines = idx + 1
    # Save statistics
    data.procesed = True
    data.read_lines = read_lines
    data.insert_lines = insert_lines
    data.update_lines = update_lines
    data.save()
  return {
    'ststus':have_errors,
    'read_lines':read_lines,
    'insert_lines':insert_lines,
    'update_lines':update_lines,
    'error_lines':error_lines,
    'error_detail':result_error
  }

class SearchSymptomData(View):
  template_name = "decisiontree/SearchSymptomData.html"
  def get(self, request, *args, **kwargs):
    form = SymptomSearchForm()
    data = {}
    data['symptom_name']=""
    data['symptom_tree'] = []
    #data['show_progress_bar']=False
    #data['show_form']=True
    #data['show_buttons']=True
    #data['show_final_progress_bar']=False
    return render(request, self.template_name,{"form": form,'data':data})

  def post(self, request, *args, **kwargs):
    form = SymptomSearchForm(request.POST)
    if form.is_valid():
      #form_object = form.save()
      #print(form_object)
      data={}
      data['symptom_name']=form.cleaned_data['symptom_name']
      data['symptom_tree']=get_symptom_tree(form.cleaned_data['symptom_id'])
      #data['symptom_name']=
      #messages.success(request, "Los datos de sintomas fueron actualizados exitosamente.")
      return render(request, self.template_name,{"form": form,'data':data})
      #return HttpResponseRedirect('/decisiontree/upload/'+str(form_object.id)+'/')
    else:
      data = {}
      data['show_buttons']=True
    return render(request, self.template_name,{"form": form,'data':data})

def get_symptom_tree(symptom_id):
    qs = SymptomDataDetail.objects.get(idx=symptom_id)
    print("************* q1 *************")
    print(qs.n1)
    qs_1 = SymptomDataDetail.objects.filter(n1=qs.n1,n3='0').exclude(n2=0)
    # qs_1 = SymptomDataDetail, n2  not in ['0'] ,n3 = '0')
    print("************** qs_1 ***********")
    print (qs_1)
    result = []
    level_dict = {}
    level_dict['text'] = qs.name
    level_dict['id'] = qs.idx
    level_state = {}
    level_state['opened'] = 'true'
    level_dict['state'] = level_state
    #result.append(qs.name)
    print(result)
    result_child = []
    result_child_n3 = []
    for row in qs_1:
        symptom_json = {}
        symptom_json['text']=row.name
        symptom_json['id']=row.idx
        symptom_json['opened']= 'true'
        # # prueba nivel 3
        result_child_n3 = []
        result_child_n4 = []
        result_child_n5 = []
        #symptom_json_n3 = {}
        # symptom_json_n3['text'] = 'Otro Nivel'
        # symptom_json_n3['id']= '000000'
        # symptom_json_n3['opened'] = 'true'
        qs_2 = SymptomDataDetail.objects.filter(n1=row.n1,n2=row.n2,level=2).exclude(n3=0)
        print('************ Contained ***********')
        print(qs_2)
        print('************ count contained')
        print(qs_2.count())
        print('************ End Contained *********')
        #result_child_n3.append(symptom_json_n3)
        # fin prueba 3
        if(qs_2.count() != 0):
            for child_rows in qs_2:
                symptom_json_n3 = {}
                symptom_json_n3['text'] = child_rows.name
                symptom_json_n3['id']= child_rows.idx
                #symptom_json_n3['opened'] = 'true'
                level_state = {}
                level_state['opened'] = 'true'
                symptom_json_n3['state'] = level_state
                # Search level 3 symptoms
                qs_3 = SymptomDataDetail.objects.filter(n1=child_rows.n1,n2=child_rows.n2,n3=child_rows.n3,level=3).exclude(n4=0)
                print('************* content 3 ***********')
                print(qs_3.count())
                print('************* end content 3 ***********')
                # if(qs_3.count() != 0):
                #     for child_child_rows in qs_3:
                #         symptom_json_n4 = {}
                #         symptom_json_n4['text'] = child_rows.name
                #         symptom_json_n4['id'] = child_rows.idx
                #         result_child_n4.append(symptom_json_n4)
                if(qs_3.count() != 0):
                    for child_child_rows in qs_3:
                        symptom_json_n4 = {}
                        symptom_json_n4['text'] = child_child_rows.name
                        symptom_json_n4['id'] = child_child_rows.idx
                        result_child_n4.append(symptom_json_n4)
                        # Search level 4 symptoms
                        qs_4 = SymptomDataDetail.objects.filter(n1=child_child_rows.n1,n2=child_child_rows.n2,n3=child_child_rows.n3,n4=child_child_rows.n4,level=4).exclude(n5=0)
                        print('************** level 4')
                        print(qs_4.count())
                        print('************** end level 4')
                        if(qs_4.count() != 0):
                            for child_rows_4 in qs_4:
                                symptom_json_n5 = {}
                                symptom_json_n5['text'] = child_rows_4.name
                                symptom_json_n5['id'] = child_rows_4.idx
                                result_child_n5.append(symptom_json_n5)
                            symptom_json_n4['children'] = result_child_n5
                    symptom_json_n3['children'] = result_child_n4
                result_child_n3.append(symptom_json_n3)
            symptom_json['children'] = result_child_n3
        result_child.append(symptom_json)
    level_dict['children'] = result_child
    print(level_dict)
    result.append(level_dict)
    print('*************** Final *****************')
    print(result)
    print('*************** end Final ****************')
    return result