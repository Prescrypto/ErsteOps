#from django.conf.urls import url, path 
from django.urls import include, path
from paperless.views import  MedicalReportNew, MedicalReportList, MedicalReportDetail, MedicalReportActive, new_medicalreport

# urlpatterns = [
#     url(r'^new/(?P<pk>[0-9]+)/$',MedicalReportNew.as_view(), name="medicalreportnew"),
#     url(r'^new/$',MedicalReportNew.as_view(), name="medicalreportnew"),
#     url(r'^',MedicalReportList.as_view(), name="medicalreportlist"),
#     url(r'^detail/(?P<pk>[0-9]+)/$',MedicalReportDetail.as_view(), name="medical_report_detail"),
# ]


urlpatterns = [
    path('new/<int:pk>/',MedicalReportNew.as_view(), name="medicalreportnew"),
    path('new/',MedicalReportNew.as_view(), name="medicalreportnew"),
    path('',MedicalReportList.as_view(), name="medicalreportlist"),
    path('detail/<int:pk>/',MedicalReportDetail.as_view(), name="medical_report_detail"),
    path('active/', MedicalReportActive.as_view(), name= "medical_report_active"),
    path('ajax/new/', new_medicalreport, name= "ajax_new_medical_report"),
]