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

# Create your views here.
class BaseReport(View):
    template_name = "reports/basereport.html"
    def get(self, request, *args, **kwargs):

        qs = Emergency.objects.filter().annotate(events=Value(1, IntegerField()))
        qs_json = serializers.serialize('json', qs)
        print("******* base data ************")
        results = []
        for record in qs:
            print(record.events)
            print(record.created_at)
            emergency_json = {
                "zone_id": record.zone.name,
                "created_at": record.created_at.strftime("%Y-%m-%d"),
                "events": 1,

            }
            results.append(emergency_json)
        data = json.dumps(results)
        # data pivoting
        #pivot_table = pivot(data,'zone_id','created_at','events')

        return render(request, self.template_name,{"form": "","data":qs_json,"clean_data":data})

