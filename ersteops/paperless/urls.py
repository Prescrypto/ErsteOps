from django.conf.urls import url
from .views import  MedicalReportNew, MedicalReportList

urlpatterns = [
    url(r'^new/$',MedicalReportNew.as_view(), name="medicalreportnew"),
    url(r'^',MedicalReportList.as_view(), name="medicalreportlist"),

]