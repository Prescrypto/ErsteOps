from django.conf.urls import url
from . import views
from reports.views import BaseReport, GeoReport

urlpatterns = [
    url(r'^$', BaseReport.as_view(), name="reportbase"),
    url(r'^georeport/$', GeoReport.as_view(), name="georeport"),
]
