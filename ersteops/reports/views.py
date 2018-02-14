# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import View

#django-pivot stuff
from django_pivot.pivot import pivot
from emergency.models import Emergency
from django.db.models import Count

from django.http import JsonResponse
from django.core import serializers
import json
import datetime

from django.db.models import Value, IntegerField
from reports.forms import SimpleDateSelector
#Date
from datetime import date, timedelta, datetime
import datetime
import calendar
from django.utils import timezone
import pytz
from collections import defaultdict

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
        # Get basic data
        form = SimpleDateSelector()
        # Get initial dates
        start_dates = initialize_dates(-6)
        start_date = start_dates[0]
        end_date = start_dates[1]
        print("********** dates *********")
        print(start_date)
        print(end_date)
        qs = Emergency.objects.filter(created_at__range=[start_date,end_date]).annotate(events=Value(1, IntegerField()))
        #qs_json = serializers.serialize('json', qs)
        data = json.dumps(clean_data(qs),default=date_handler)
        # data pivoting
        #pivot_table = pivot(qs,'zone_id','created_at','events')
        return render(request, self.template_name,{"form": form,"data":data,"clean_data":data,})

    def post(self, request, *args, **kwargs):
        form = SimpleDateSelector(request.POST)
        if form.is_valid():
            qs = Emergency.objects.filter(created_at__range=[form.cleaned_data['from_date'],form.cleaned_data['until_date']]).annotate(events=Value(1, IntegerField()))
            #qs_json = serializers.serialize('json', qs)
            data = json.dumps(clean_data(qs),default=date_handler)
            #pivot_table = pivot(qs,'zone_id','created_at','events')
        return render(request, self.template_name,{"form": form,"data":data,"clean_data":data,})


def clean_data(qs):
    results = []
    for record in qs:
        #print(record.events)
        #print(record.created_at)
        #print(str(record.emergencyTimer))
        emergency_json = {
            "Zona": record.zone.name,
            "Genero": record.patient_gender,
            "Grado": record.grade_type.name,
            "Tipo Subscripcion": record.subscription_type,
            #"unit_type": record.units.unit_type[0],
            #"attention_final_grade":record.attention_final_grade.name,
            "Fecha": record.created_at.strftime("%Y-%m-%d"),
            "Año": record.created_at.strftime("%Y"),
            "Mes": record.created_at.strftime("%m"),
            "Semana": record.created_at.strftime("%W"),
            #"created_at": record.created_at,
            "Incidencias": record.events,
            "Tipo Emergencia": record.service_category.name,
            "Tiempo de Atención": str(record.final_emergency_time-record.start_time),
            "Tiempo de Llegada": str(record.arrival_time-record.start_time),
            "Tiempo de atención efectiva": str(record.attention_time-record.start_time),
            "Tiempo de Asignación de Unidad": str(record.unit_assigned_time-record.start_time),
            "Tiempo de Despacho de Unidad": str(record.unit_dispatched_time-record.start_time),


        }
        results.append(emergency_json)
    return results



