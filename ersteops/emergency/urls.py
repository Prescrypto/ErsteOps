from django.conf.urls import url
from . import views
from emergency.views import (
    EmergencyNew, 
    EmergencyDashboardList, 
    EmergencyActivate, 
    EmergencyEnd, 
    EmergencyJSONView,
    EmergencyJSONGetPatient, 
    EmergencyJsonEnd,
    EmergencyJSONUpdate, 
    EmergencyText, 
    grade_view, 
    timer_view,
    derivation_view,
    hospital_json_list,
)

urlpatterns = [
    url(r'^new/$', EmergencyNew.as_view(), name="emergencynew"),
    url(r'^new/(?P<pk>[0-9]+)', EmergencyJSONUpdate.as_view(), name="emergency_json_update"),
    url(r'^dashboard/$', EmergencyDashboardList.as_view(), name="emergencydashboard"),
    url(r'^detail_text/(?P<emergency_id>[0-9]+)/$', EmergencyText.as_view(), name='emergencytext'),
    url(r'^activate/(?P<patient_id>\d+)/$', EmergencyActivate.as_view(), name='emergencyactivate'),
    url(r'^end/(?P<patient_id>\d+)/$', EmergencyEnd.as_view(), name='emergencend'),
    # Ajax Views for emergencies!
    url(r'^ajax/end/(?P<patient_id>\d+)/$', EmergencyJsonEnd.as_view(), name="emergency_json_end"),
    url(r'^ajax/detail/(?P<pk>[0-9]+)/$', EmergencyJSONView.as_view(), name="emergency_json_detail"),
    url(r'^ajax/patient/(?P<patient_id>[0-9]+)/$', EmergencyJSONGetPatient.as_view(), name="emergency_patient_json"),
    url(r'^ajax/change_grade/$', grade_view, name="ajax_change_grade"),
    url(r'^ajax/update_timer/$', timer_view, name="ajax_update_timer"),
    url(r'^ajax/update_derivation/$', derivation_view, name="ajax_update_derivation"),
    url(r'^ajax/hospital/$', hospital_json_list, name="hospital_json_list"),
]
