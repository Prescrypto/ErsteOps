from django.conf.urls import url
from . import views
from emergency.views import (
    EmergencyBlank, EmergencyNew, EmergencyListView,
    EmergencyDetailView, EmergencyDashboardList, EmergencyDerivation,
    EmergencyUpdate, EmergencyClientOdoo, EmergencyClientModal,
    EmergencyNewModal, EmergencyGetPatient, OdooSubscription,
    EmergencyActivate, EmergencyEnd, EmergencyJSONView,
    EmergencyJSONGetPatient, EmergencyListJSONView
)

urlpatterns = [
    url(r'^$', EmergencyBlank.as_view(), name="emergencyblank"),
    url(r'^new/$', EmergencyNew.as_view(), name="emergencynew"),
    url(r'^list/$', EmergencyListView.as_view(), name="emergencylist"),
    url(r'^modal/$', EmergencyClientModal.as_view(), name="odoomodal"),
    url(r'^newmodal/$', EmergencyNewModal.as_view(), name="newincidentmodal"),
    url(r'^subscriptor/$', OdooSubscription.as_view(), name="subscriptormodal"),
    url(r'^odooapi/$', EmergencyClientOdoo.as_view(), name="emergencyodoo"),
    url(r'^update/(?P<pk>[0-9]+)/$', EmergencyUpdate.as_view(), name="emergencyupdate"),
    url(r'^dashboard/$', EmergencyDashboardList.as_view(), name="emergencydashboard"),
    url(r'^derivation/$', EmergencyDerivation.as_view(), name="emergencyderivation"),
    url(r'^(?P<pk>[0-9]+)/$', EmergencyDetailView.as_view(), name='emergencydetail'),
    url(r'^activate/(?P<patient_id>\d+)/$', EmergencyActivate.as_view(), name='emergencyactivate'),
    url(r'^end/(?P<patient_id>\d+)/$', EmergencyEnd.as_view(), name='emergencend'),
    url(r'^getpatient/(?P<patient_id>\d+)/$', EmergencyGetPatient.as_view(), name='emergencypatient'),
    # Ajax Views for emergencies!
    url(r'^ajax/list/$', EmergencyListJSONView.as_view(), name="emergency_json_list"),
    url(r'^ajax/detail/(?P<pk>[0-9]+)/$', EmergencyJSONView.as_view(), name="emergency_json_detail"),
    url(r'^ajax/patient/(?P<patient_id>[0-9]+)/$', EmergencyJSONGetPatient.as_view(), name="emergency_patient_json"),
]
