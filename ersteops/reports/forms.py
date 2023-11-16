# -*- encoding: utf-8 -*-
from django import forms
#from django.forms import extras
from django.forms.widgets import SelectDateWidget

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
      widget=forms.SelectDateWidget(
              years=range(2014, 2026),attrs={'class': 'uk-width-1-2 ui-form-controls c-btn c-btn--secondary has-dropdown dropdown-toggle'}
          ))
  until_date = forms.DateField(
      required=True,
      label='Hasta:',
      initial=date(utc_mx.year,utc_mx.month,utc_mx.day),
      widget=forms.SelectDateWidget(
              years=range(2014, 2026),attrs={'class': 'uk-form-controls c-btn c-btn--secondary has-dropdown dropdown-toggle'}
          ))
