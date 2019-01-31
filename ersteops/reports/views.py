# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import View

#django-pivot stuff
from django_pivot.pivot import pivot
from emergency.models import Emergency
from unit.models import Unit
from django.db.models import Count

from django.http import JsonResponse
from django.core import serializers
import json
import datetime

from django.db.models import Value, IntegerField, DateTimeField, DateField, F, CharField, DurationField, TimeField
from reports.forms import SimpleDateSelector
#Date
from datetime import date, timedelta, datetime
import datetime
import calendar
from django.utils import timezone
import pytz
from collections import defaultdict
# database functions to use in queryset
from django.db.models.functions import (ExtractDay, ExtractMonth, ExtractWeek,ExtractWeekDay, ExtractYear, Trunc, Cast)

from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
# ********************
# begin date stuff
#Add TIME_ZONE constant to use in get_utc method
TIME_ZONE = "America/Mexico_City"
# This method return the given time zone UTC
# Can use a diferent Time Zone with time_zone parameter
def get_utc(time_zone=TIME_ZONE):
  # Read current UTC datetime
  utc = pytz.utc.localize(datetime.datetime.utcnow())
  # Set users time zone
  instance_time_zone = pytz.timezone(time_zone)
  # Convert current UTC to user tome zone
  return utc.astimezone(instance_time_zone)

# Get month difference
def diff_month(start_date, end_date):
    return (start_date.year - end_date.year)*12 + start_date.month - end_date.month

# Method that adds months to a date... returns a full datetime object
def add_months(sourcedate, months):
  month = sourcedate.month - 1 + months
  year = int(sourcedate.year + month / 12 )
  month = month % 12 + 1
  day = min(sourcedate.day, calendar.monthrange(year,month)[1])
  return datetime.date(year,month,day)

# Get intial date array for all queries
def initialize_dates(months_before):
   # Called to get_utc method
    utc_mx = get_utc()

    start_date = add_months(utc_mx, months_before)
    end_date = date(utc_mx.year,utc_mx.month,utc_mx.day)
    return [datetime.date(start_date.year,start_date.month,1), end_date]

def date_handler(obj):
    ''' Function to manage date and datetime objects in json '''
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError ("Type %s not serializable" % type(obj))
# ********************

class BaseReport(View):
    template_name = "reports/basereport_1.html"
    def get(self, request, *args, **kwargs):
        form = SimpleDateSelector()
        # Get initial dates
        start_dates = initialize_dates(-6)
        start_date = start_dates[0]
        end_date = start_dates[1]
        # Get basic data
        data = getBaseData(start_date,end_date)
        #print("******************************************")
        #print(data)
        return render(request, self.template_name,{"form": form,"data":data,})

    def post(self, request, *args, **kwargs):
        form = SimpleDateSelector(request.POST)
        if form.is_valid():
            data = getBaseData(form.cleaned_data['from_date'],form.cleaned_data['until_date'])
        return render(request, self.template_name,{"form": form,"data":data,})


# Get queryset and return json
def getBaseData(start_date,end_date):
    correct_end_date = end_date + datetime.timedelta(days=1)
    qs= Emergency.objects.filter(created_at__range=[start_date,correct_end_date]).values(
            'id',
            #'zone',
            #'patient_gender',
            #'units__unit_type',
            #'grade_type',
            #'subscription_type',
            #'created_at',
            #'service_category__name'
            ).annotate(
            Grado=F('grade_type'),
            Grado_Final=F('attention_final_grade'),
            Zona=F('zone'),
            #Patient Data
            Genero=F('patient_gender'),
            Paciente=F('patient_name'),
            Edad=F('patient_age'),
            No_Socio=F('odoo_client'),
            Convenio=F('erste_code'),
            Calle_y_Numero=F('address_street'),
            Calle=F('address_extra'),
            Codigo_Postal=F('address_zip_code'),
            Delegacion=F('address_county'),
            Colonia=F('address_col'),
            Tipo_Unidad=F('units__unit_type'),
            Sintomas_Principal=F('main_complaint'),
            Categoria_Servicio=F('service_category__name'),
            Tipo_Subscripcion=F('subscription_type'),
            Año=ExtractYear('created_at'),
            Semana=ExtractWeek('created_at'),
            Mes=ExtractMonth('created_at'),
            Fecha=Trunc('created_at', 'day', output_field=DateField()),
            Tiempo_de_Atencion=F('final_emergency_time')-F('start_time'),
            #Tiempo_de_Atencion=Cast(F('final_emergency_time')-F('start_time'),TimeField()),
            Tiempo_de_Llegada=Cast(F('arrival_time')-F('start_time'),TimeField()),
            Tiempo_de_Atención_Efectiva=Cast(F('attention_time')-F('start_time'),TimeField()),
            Tiempo_de_Asignación_de_Unidad=Cast(F('unit_assigned_time')-F('start_time'),TimeField()),
            Tiempo_de_Despacho_de_Unidad=Cast(F('unit_dispatched_time')-F('start_time'),TimeField()),
            #duracion=(F('final_emergency_time')-F('start_time'),CharField()),
            )
    #print(qs)
    return json.dumps(list(qs), cls=DjangoJSONEncoder)
