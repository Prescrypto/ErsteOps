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
      #data['symptom_tree']=get_symptom_tree(form.cleaned_data['symptom_id'])
      data['symptom_tree']=get_symptom_tree_zero(form.cleaned_data['symptom_id'])
      #data['symptom_name']=
      #messages.success(request, "Los datos de sintomas fueron actualizados exitosamente.")
      return render(request, self.template_name,{"form": form,'data':data})
      #return HttpResponseRedirect('/decisiontree/upload/'+str(form_object.id)+'/')
    else:
      data = {}
      data['show_buttons']=True
    return render(request, self.template_name,{"form": form,'data':data})

class SearchSymptomData2(View):
  template_name = "decisiontree/SearchSymptomData_2.html"
  def get(self, request, *args, **kwargs):
    form = SymptomSearchForm()
    data = {}
    data['symptom_name']=""
    data['symptom_tree'] = []
    data['vue_symptom_tree'] = []
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
      #data['symptom_tree']=get_symptom_tree(form.cleaned_data['symptom_id'])
      data['symptom_tree']=get_symptom_tree_zero(form.cleaned_data['symptom_id'])
      data['vue_symptom_tree']=get_vue_symptom_tree_zero(form.cleaned_data['symptom_id'])
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
    for child_row_1 in qs_1:
        symptom_json = {}
        symptom_json['text'] = '1' + child_row_1.name 
        symptom_json['id'] = child_row_1.idx
        symptom_json['opened'] = 'true'
        # # prueba nivel 3
        result_child_n3 = []
        result_child_n4 = []
        result_child_n5 = []
        result_child_n6 = []
        result_child_n7 = []
        #symptom_json_n3 = {}
        # symptom_json_n3['text'] = 'Otro Nivel'
        # symptom_json_n3['id']= '000000'
        # symptom_json_n3['opened'] = 'true'
        qs_2 = SymptomDataDetail.objects.filter(n1=child_row_1.n1,n2=child_row_1.n2,level=2).exclude(n3=0)
        print('************ Contained ***********')
        print(qs_2)
        print('************ count contained')
        print(qs_2.count())
        print('************ End Contained *********')
        #result_child_n3.append(symptom_json_n3)
        # fin prueba 3
        if(qs_2.count() != 0):
            for child_rows_2 in qs_2:
                symptom_json_n3 = {}
                symptom_json_n3['text'] = '2' + child_rows_2.name
                symptom_json_n3['id'] = child_rows_2.idx
                #symptom_json_n3['opened'] = 'true'
                level_state = {}
                level_state['opened'] = 'true'
                symptom_json_n3['state'] = level_state
                # Search level 3 symptoms
                qs_3 = SymptomDataDetail.objects.filter(n1=child_rows_2.n1,n2=child_rows_2.n2,n3=child_rows_2.n3,level=3).exclude(n4=0)
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
                    for child_rows_3 in qs_3:
                        symptom_json_n4 = {}
                        symptom_json_n4['text'] = '3' + child_rows_3.name
                        symptom_json_n4['id'] = child_rows_3.idx
                        result_child_n4.append(symptom_json_n4)
                        # Search level 4 symptoms
                        qs_4 = SymptomDataDetail.objects.filter(n1=child_rows_3.n1,n2=child_rows_3.n2,n3=child_rows_3.n3,n4=child_rows_3.n4,level=4).exclude(n5=0)
                        print('************** level 4')
                        print(qs_4.count())
                        print('************** end level 4')
                        if(qs_4.count() != 0):
                            result_child_n5 = []
                            for child_rows_4 in qs_4:
                                symptom_json_n5 = {}
                                symptom_json_n5['text'] = '4' + child_rows_4.name
                                symptom_json_n5['id'] = child_rows_4.idx
                                result_child_n5.append(symptom_json_n5)

                                # start symptom 5
                                # Search level 5 symptoms
                                #qs_4 = SymptomDataDetail.objects.filter(n1=child_rows_3.n1,n2=child_rows_3.n2,n3=child_rows_3.n3,n4=child_rows_3.n4,level=4).exclude(n5=0)
                                qs_5 = SymptomDataDetail.objects.filter(n1=child_rows_4.n1,n2=child_rows_4.n2,n3=child_rows_4.n3,n4=child_rows_4.n4,n5=child_rows_4.n5,n6=child_rows_4.n6,level=5).exclude(n6=0,n5=0)
                                print('************** level 5')
                                print(child_rows_4)
                                print(qs_5.count())
                                print('************** end level 5')

                                if(qs_5.count() != 0):
                                    result_child_n6 = []
                                    for child_rows_5 in qs_5:
                                        symptom_json_n6 = {}
                                        symptom_json_n6['text'] = '5' + child_rows_5.name
                                        symptom_json_n6['id'] = child_rows_5.idx
                                        result_child_n6.append(symptom_json_n6)
                                        # start symptom 6
                                        # end symptom 6
                                    symptom_json_n5['children'] = result_child_n6
                                # end symptom 5

                            symptom_json_n4['children'] = result_child_n5
                    symptom_json_n3['children'] = result_child_n4
                result_child_n3.append(symptom_json_n3)
            symptom_json['children'] = result_child_n3
        result_child.append(symptom_json)
    level_dict['children'] = result_child
    #print(level_dict)
    result.append(level_dict)
    print('*************** Final *****************')
    print(result)
    print('*************** end Final ****************')
    return result


def get_symptom_tree_zero(symptom_id):
    # Get Symptom Zero data
    qs_0 = SymptomDataDetail.objects.get(idx=symptom_id)
    # Begin fill level zero
    result_0 = []
    level_dict_0 = {}
    level_dict_0['text'] = '('+ qs_0.symptom_type.name +') ' + qs_0.name
    level_dict_0['id'] = qs_0.idx
    level_state_0 = {}
    level_state_0['opened'] = 'true'
    level_dict_0['state'] = level_state_0
    # Level one query set
    tree_level = get_correct_symtom_type(qs_0.symptom_type,qs_0.level)
    qs_01 = SymptomDataDetail.objects.filter(n1=qs_0.key,level=tree_level,symptom_type=qs_0.symptom_type) #.exclude(n2=0)

    result_level_1 = []
    #result_level_2 = []
    if(qs_01.count() != 0):
        for child_rows_01 in qs_01:
            level_dict_1 = {}
            level_dict_1['text'] = child_rows_01.name
            level_dict_1['id'] = child_rows_01.idx
            result_level_1.append(level_dict_1)
            #result_level_1.append(get_symtom_tree_format(child_rows_01))
            # Begin Search Next Level
            print('##############################################')
            print('**************** Parent Tree Level ***********')
            print(child_rows_01.level)
            tree_level = get_correct_symtom_type(child_rows_01.symptom_type,child_rows_01.level)
            get_print_parameters(child_rows_01,tree_level)
            print('**************** Next Tree Level *************')
            print(tree_level)
            qs_02 = SymptomDataDetail.objects.filter(n1=child_rows_01.n1 ,n2=child_rows_01.n2, level=tree_level,symptom_type=child_rows_01.symptom_type).exclude(n3='0')
            print('**************** QS2 ******************')
            #print(qs_02)

            if(qs_02.count() != 0):
                result_level_2 = []
                for child_rows_2 in qs_02:
                    level_dict_2 = {}
                    level_dict_2['text'] = child_rows_2.name
                    level_dict_2['id'] = child_rows_2.idx
                    result_level_2.append(level_dict_2)
                    # Begin Search Next Level
                    print('**************** Parent Tree Level ***********')
                    print(child_rows_2.level)
                    tree_level = get_correct_symtom_type(child_rows_2.symptom_type,child_rows_2.level)
                    get_print_parameters(child_rows_2,tree_level)
                    print('**************** Next Tree Level *************')
                    print(tree_level)
                    qs_03 = SymptomDataDetail.objects.filter(n1=child_rows_2.n1 ,n2=child_rows_2.n2,n3=child_rows_2.n3, level=tree_level,symptom_type=child_rows_2.symptom_type).exclude(n4=0)
                    print('**************** QS3 ******************')
                    #print(qs_03)
                    if(qs_03.count() != 0):
                        result_level_3 = []
                        for child_rows_3 in qs_03:
                            level_dict_3 = {}
                            level_dict_3['text'] = child_rows_3.name
                            level_dict_3['id'] = child_rows_3.idx
                            result_level_3.append(level_dict_3)

                            # Begin Search Next Level
                            print('**************** Parent Tree Level ***********')
                            print(child_rows_3.level)
                            tree_level = get_correct_symtom_type(child_rows_3.symptom_type,child_rows_3.level)
                            get_print_parameters(child_rows_3,tree_level)
                            print('**************** Next Tree Level *************')
                            print(tree_level)
                            qs_04 = SymptomDataDetail.objects.filter(n1=child_rows_3.n1 ,n2=child_rows_3.n2,n3=child_rows_3.n3,n4=child_rows_3.n4, level=tree_level,symptom_type=child_rows_3.symptom_type).exclude(n5='0')
                            print('**************** QS4 ******************')
                            #print(qs_04)
                            if(qs_04.count() != 0):
                                result_level_4 = []
                                for child_rows_4 in qs_04:
                                    level_dict_4 = {}
                                    level_dict_4['text'] = '4-'+ child_rows_4.name
                                    level_dict_4['id'] = child_rows_4.idx
                                    result_level_4.append(level_dict_4)

                                    # # Begin Search Next Level
                                    print('**************** Parent Tree Level ***********')
                                    print(child_rows_4.level)
                                    tree_level = get_correct_symtom_type(child_rows_4.symptom_type,child_rows_4.level)
                                    get_print_parameters(child_rows_4,tree_level)
                                    print('**************** Next Tree Level *************')
                                    print(tree_level)
                                    qs_05 = SymptomDataDetail.objects.filter(n1=child_rows_4.n1 ,n2=child_rows_4.n2,n3=child_rows_4.n3,n4=child_rows_4.n4,n5=child_rows_4.n5, level=tree_level,symptom_type=child_rows_4.symptom_type).exclude(n6='0')
                                    print('**************** QS5 ******************')
                                    print(qs_05)
                                    if(qs_05.count() != 0):
                                        result_level_5 = []
                                        for child_rows_5 in qs_05:
                                            level_dict_5 = {}
                                            level_dict_5['text'] = child_rows_5.name
                                            level_dict_5['id'] = child_rows_5.idx
                                            result_level_5.append(level_dict_5)

                                            # # Begin Search Next Level
                                            print('**************** Parent Tree Level ***********')
                                            print(child_rows_5.level)
                                            tree_level = get_correct_symtom_type(child_rows_5.symptom_type,child_rows_5.level)
                                            get_print_parameters(child_rows_5,tree_level)
                                            print('**************** Next Tree Level *************')
                                            print(tree_level)
                                            qs_06 = SymptomDataDetail.objects.filter(n1=child_rows_5.n1 ,n2=child_rows_5.n2,n3=child_rows_5.n3,n4=child_rows_5.n4,n5=child_rows_5.n5, n6=child_rows_5.n6,level=tree_level,symptom_type=child_rows_5.symptom_type).exclude(n7='0')
                                            print('**************** QS6 ******************')
                                            print(qs_06)
                                            if(qs_06.count() != 0):
                                                result_level_6 = []
                                                for child_rows_6 in qs_06:
                                                    level_dict_6 = {}
                                                    level_dict_6['text'] = child_rows_6.name
                                                    level_dict_6['id'] = child_rows_6.idx
                                                    result_level_6.append(level_dict_6)



                                                level_dict_5['children'] = result_level_6
                                            # # End Search Next Level

                                        level_dict_4['children'] = result_level_5
                                    # # End Search Next Level

                                level_dict_3['children'] = result_level_4
                            # End Search Next Level

                        level_dict_2['children'] = result_level_3
                    # End Search Next Level
                level_dict_1['children'] = result_level_2
            # End Search Next Level
        level_dict_0['children'] = result_level_1

    result_0.append(level_dict_0)
    print('*************** Final Tree *****************')
    #print(result_0)
    print('*************** end Final ****************')
    return result_0

def get_vue_symptom_tree_zero(symptom_id):
    # Get Symptom Zero data
    qs_0 = SymptomDataDetail.objects.get(idx=symptom_id)
    # Begin fill level zero
    result_0 = []
    level_dict_0 = {}
    level_dict_0['label'] = '('+ qs_0.symptom_type.name +') ' + qs_0.name
    level_dict_0['id'] = qs_0.idx
    level_state_0 = {}
    level_state_0['opened'] = 'true'
    level_dict_0['state'] = level_state_0
    # Level one query set
    tree_level = get_correct_symtom_type(qs_0.symptom_type,qs_0.level)
    qs_01 = SymptomDataDetail.objects.filter(n1=qs_0.key,level=tree_level,symptom_type=qs_0.symptom_type) #.exclude(n2=0)

    result_level_1 = []
    #result_level_2 = []
    if(qs_01.count() != 0):
        for child_rows_01 in qs_01:
            level_dict_1 = {}
            level_dict_1['label'] = child_rows_01.name
            level_dict_1['id'] = child_rows_01.idx
            result_level_1.append(level_dict_1)
            #result_level_1.append(get_symtom_tree_format(child_rows_01))
            # Begin Search Next Level
            #print('##############################################')
            #print('**************** Parent Tree Level ***********')
            #print(child_rows_01.level)
            tree_level = get_correct_symtom_type(child_rows_01.symptom_type,child_rows_01.level)
            #get_print_parameters(child_rows_01,tree_level)
            #print('**************** Next Tree Level *************')
            #print(tree_level)
            qs_02 = SymptomDataDetail.objects.filter(n1=child_rows_01.n1 ,n2=child_rows_01.n2, level=tree_level,symptom_type=child_rows_01.symptom_type).exclude(n3='0')
            #print('**************** QS2 ******************')
            #print(qs_02)

            if(qs_02.count() != 0):
                result_level_2 = []
                for child_rows_2 in qs_02:
                    level_dict_2 = {}
                    level_dict_2['label'] = child_rows_2.name
                    level_dict_2['id'] = child_rows_2.idx
                    result_level_2.append(level_dict_2)
                    # Begin Search Next Level
                    #print('**************** Parent Tree Level ***********')
                    #print(child_rows_2.level)
                    tree_level = get_correct_symtom_type(child_rows_2.symptom_type,child_rows_2.level)
                    #get_print_parameters(child_rows_2,tree_level)
                    #print('**************** Next Tree Level *************')
                    #print(tree_level)
                    qs_03 = SymptomDataDetail.objects.filter(n1=child_rows_2.n1 ,n2=child_rows_2.n2,n3=child_rows_2.n3, level=tree_level,symptom_type=child_rows_2.symptom_type).exclude(n4=0)
                    #print('**************** QS3 ******************')
                    #print(qs_03)
                    if(qs_03.count() != 0):
                        result_level_3 = []
                        for child_rows_3 in qs_03:
                            level_dict_3 = {}
                            level_dict_3['label'] = child_rows_3.name
                            level_dict_3['id'] = child_rows_3.idx
                            result_level_3.append(level_dict_3)

                            # Begin Search Next Level
                            #print('**************** Parent Tree Level ***********')
                            #print(child_rows_3.level)
                            tree_level = get_correct_symtom_type(child_rows_3.symptom_type,child_rows_3.level)
                            #get_print_parameters(child_rows_3,tree_level)
                            #print('**************** Next Tree Level *************')
                            #print(tree_level)
                            qs_04 = SymptomDataDetail.objects.filter(n1=child_rows_3.n1 ,n2=child_rows_3.n2,n3=child_rows_3.n3,n4=child_rows_3.n4, level=tree_level,symptom_type=child_rows_3.symptom_type).exclude(n5='0')
                            #print('**************** QS4 ******************')
                            #print(qs_04)
                            if(qs_04.count() != 0):
                                result_level_4 = []
                                for child_rows_4 in qs_04:
                                    level_dict_4 = {}
                                    level_dict_4['label'] = '4-'+ child_rows_4.name
                                    level_dict_4['id'] = child_rows_4.idx
                                    result_level_4.append(level_dict_4)

                                    # # Begin Search Next Level
                                    #print('**************** Parent Tree Level ***********')
                                    #print(child_rows_4.level)
                                    tree_level = get_correct_symtom_type(child_rows_4.symptom_type,child_rows_4.level)
                                    #get_print_parameters(child_rows_4,tree_level)
                                    #print('**************** Next Tree Level *************')
                                    #print(tree_level)
                                    qs_05 = SymptomDataDetail.objects.filter(n1=child_rows_4.n1 ,n2=child_rows_4.n2,n3=child_rows_4.n3,n4=child_rows_4.n4,n5=child_rows_4.n5, level=tree_level,symptom_type=child_rows_4.symptom_type).exclude(n6='0')
                                    #print('**************** QS5 ******************')
                                    #print(qs_05)
                                    if(qs_05.count() != 0):
                                        result_level_5 = []
                                        for child_rows_5 in qs_05:
                                            level_dict_5 = {}
                                            level_dict_5['label'] = child_rows_5.name
                                            level_dict_5['id'] = child_rows_5.idx
                                            result_level_5.append(level_dict_5)

                                            # # Begin Search Next Level
                                            #print('**************** Parent Tree Level ***********')
                                            #print(child_rows_5.level)
                                            tree_level = get_correct_symtom_type(child_rows_5.symptom_type,child_rows_5.level)
                                            #get_print_parameters(child_rows_5,tree_level)
                                            #print('**************** Next Tree Level *************')
                                            #print(tree_level)
                                            qs_06 = SymptomDataDetail.objects.filter(n1=child_rows_5.n1 ,n2=child_rows_5.n2,n3=child_rows_5.n3,n4=child_rows_5.n4,n5=child_rows_5.n5, n6=child_rows_5.n6,level=tree_level,symptom_type=child_rows_5.symptom_type).exclude(n7='0')
                                            #print('**************** QS6 ******************')
                                            #print(qs_06)
                                            if(qs_06.count() != 0):
                                                result_level_6 = []
                                                for child_rows_6 in qs_06:
                                                    level_dict_6 = {}
                                                    level_dict_6['label'] = child_rows_6.name
                                                    level_dict_6['id'] = child_rows_6.idx
                                                    result_level_6.append(level_dict_6)



                                                level_dict_5['children'] = result_level_6
                                            # # End Search Next Level

                                        level_dict_4['children'] = result_level_5
                                    # # End Search Next Level

                                level_dict_3['children'] = result_level_4
                            # End Search Next Level

                        level_dict_2['children'] = result_level_3
                    # End Search Next Level
                level_dict_1['children'] = result_level_2
            # End Search Next Level
        level_dict_0['children'] = result_level_1

    result_0.append(level_dict_0)
    #print('*************** Final Tree *****************')
    #print(result_0)
    #print('*************** end Final ****************')
    return result_0

def get_symtom_tree_level(qs):
    #qs = SymptomDataDetail.objects.filter(n1=id_key,level=id_level,symptom_type=id_symptom_type) #.exclude(n2=0)
    #print('*************** Level one ***************')
    #print('id_key:' + id_key)
    #print('id_level:' + id_level)
    #print(qs)
    #print('*****************************************')
    result = []
    if(qs.count() != 0):
        for row in qs:
            level_dict = {}
            level_dict['text'] = row.name
            level_dict['id'] = row.idx
            result.append(level_dict)
    return result

def get_symtom_tree_format(row):
    #qs = SymptomDataDetail.objects.filter(n1=id_key,level=id_level,symptom_type=id_symptom_type) #.exclude(n2=0)
    #print('*************** Level one ***************')
    #print('id_key:' + id_key)
    #print('id_level:' + id_level)
    #print(qs)
    #print('*****************************************')
    #result = []
    # if(qs.count() != 0):
    #     for row in qs:
    level_dict = {}
    level_dict['text'] = row.name
    level_dict['id'] = row.idx
    #result.append(level_dict)
    return level_dict

def get_correct_symtom_type(id_symptom_type,id_level):
    if(id_symptom_type == 2):
        correct_id_level = str(int(id_level)+1)
    else:
        correct_id_level = str(int(id_level)+1)
    return correct_id_level



def get_print_parameters(row,current_level):
    string_val = '*' *( 2* int(current_level) )
    print(string_val)
    print(string_val + '*********** Data Level ' + current_level +' *************')
    print(string_val + '- idx:         ',row.idx)
    print(string_val + '- name:        ',row.name.encode('utf-8'))
    print(string_val + '- n1:          ',row.n1)
    print(string_val + '- n2:          ',row.n2)
    print(string_val + '- n3:          ',row.n3)
    print(string_val + '- n4:          ',row.n4)
    print(string_val + '- n5:          ',row.n5)
    print(string_val + '- n6:          ',row.n6)
    print(string_val + '- n7:          ',row.n7)
    print(string_val + '- level:       ',row.level)
    print(string_val + '- grade:       ',row.grade)
    print(string_val + '- key:         ',row.key)
    print(string_val + '- symptom_type:',row.symptom_type)
    return 0