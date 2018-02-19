from django.conf.urls import url
from . import views
from reports.views import BaseReport

urlpatterns = [
    url(r'^$', BaseReport.as_view(), name="reportbase"),

]
