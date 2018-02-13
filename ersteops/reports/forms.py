# -*- encoding: utf-8 -*-
from django import forms
from django.forms import extras
#Date
from datetime import date, timedelta, datetime
# For UTC
import datetime
from django.utils import timezone
import pytz

class SimpleDateSelector(forms.Form):
  # Read current UTC datetime
  utc = pytz.utc.localize(datetime.datetime.utcnow())
  # Set users time zone
  instance_time_zone = pytz.timezone('America/Mexico_City')
  # Convert current UTC to user tome zone
  utc_mx = utc.astimezone(instance_time_zone)
  from_date = forms.DateField(
      required=True,
      label='Desde:',
      initial=date(utc_mx.year, 1, 1),
      widget=extras.SelectDateWidget(
              years=range(2014, 2020),attrs={'class': 'form-control'}
          ))
  until_date = forms.DateField(
      required=True,
      label='Hasta:',
      initial=date(utc_mx.year,utc_mx.month,utc_mx.day),
      widget=extras.SelectDateWidget(
              years=range(2014, 2020),attrs={'class': 'form-control'}
          ))