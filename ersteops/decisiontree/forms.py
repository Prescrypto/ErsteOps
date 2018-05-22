# -*- encoding: utf-8 -*-
from django import forms
from django.forms import extras
#Date
from datetime import date, timedelta, datetime
# For UTC
import datetime
from django.utils import timezone
import pytz
from .models import SymptomDataFile
#from uber.models import UploadUberData

class UploadSymptomDataFileForm(forms.ModelForm):
  class Meta:
    model = SymptomDataFile
    fields = ['name','symptom_file']
    labels = { 
              'name':'Nombre de la carga:',
              'symptom_file': 'Symptom Data File'
    }
    widgets = {
                'name': forms.TextInput(attrs={'placeholder':'eg: Input 2017/04/13','class': 'form-control'}),
                'symptom_file': forms.FileInput({'is_hidden': 'False','class': 'form-control'})
    }

  def clean_symptom_file(self):
    upload_file = self.cleaned_data.get('symptom_file', False)
    print ("************ Content type")
    print (upload_file.content_type)
    if self.files:
      main, sub = upload_file.content_type.split('/')
      print ("********** Validate file")
      print (main) 
      print (sub)
      if not (main == 'text' and sub.lower() in ['csv',]):
                raise forms.ValidationError(('Use una archivo csv,xls o xlsx.'))
    return upload_file

class SymptomSearchForm(forms.Form):
  # Begin Minimal Client Data
  symptom_id = forms.CharField(
    label = 'client_id',
    required = False,
    initial = 0,
    widget = forms.HiddenInput(attrs={'is_hidden': 'True'})
    )
  symptom_name = forms.CharField(
    label = '* Sintoma principal:',
    required = True,
    widget=forms.TextInput(attrs={
      'class': 'form-control ui-widget uk-width-1-2',
      'placeholder': 'sintoma p.ejem. ahogado',
      'max_length': '100'
      })
  )