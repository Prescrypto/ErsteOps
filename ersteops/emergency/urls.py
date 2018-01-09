from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from emergency.views import (
    EmergencyBlank, EmergencyNew, EmergencyListView,
    EmergencyDetailView, EmergencyDashboardList, EmergencyDerivation,
    EmergencyUpdate, EmergencyClientOdoo, EmergencyClientModal,
    EmergencyNewModal, EmergencyGetPatient, OdooSubscription,
    EmergencyActivate, EmergencyEnd, EmergencyJSONView,
    EmergencyJSONGetPatient, EmergencyListJSONView, EmergencyJsonEnd
)

urlpatterns = [
    url(r'^$', EmergencyBlank.as_view(), name="emergencyblank"),
    url(r'^new/$', login_required(EmergencyNew.as_view(), login_url='/'), name="emergencynew"),
    url(r'^list/$', login_required(EmergencyListView.as_view(), login_url='/'), name="emergencylist"),
    url(r'^modal/$', login_required(EmergencyClientModal.as_view(), login_url='/'), name="odoomodal"),
    url(r'^newmodal/$', login_required(EmergencyNewModal.as_view(), login_url='/'), name="newincidentmodal"),
    url(r'^subscriptor/$', login_required(OdooSubscription.as_view(), login_url='/'), name="subscriptormodal"),
    url(r'^odooapi/$', login_required(EmergencyClientOdoo.as_view(), login_url='/'), name="emergencyodoo"),
    url(r'^update/(?P<pk>[0-9]+)/$', login_required(EmergencyUpdate.as_view(), login_url='/'), name="emergencyupdate"),
    url(r'^dashboard/$', login_required(EmergencyDashboardList.as_view(), login_url='/'), name="emergencydashboard"),
    url(r'^derivation/$', login_required(EmergencyDerivation.as_view(), login_url='/'), name="emergencyderivation"),
    url(r'^(?P<pk>[0-9]+)/$', login_required(EmergencyDetailView.as_view(), login_url='/'), name='emergencydetail'),
    url(r'^activate/(?P<patient_id>\d+)/$', login_required(EmergencyActivate.as_view(), login_url='/'), name='emergencyactivate'),
    url(r'^end/(?P<patient_id>\d+)/$', login_required(EmergencyEnd.as_view(), login_url='/'), name='emergencend'),
    url(r'^getpatient/(?P<patient_id>\d+)/$', login_required(EmergencyGetPatient.as_view(), login_url='/'), name='emergencypatient'),
    # Ajax Views for emergencies!
    url(r'^ajax/list/$', login_required(EmergencyListJSONView.as_view(), login_url='/'), name="emergency_json_list"),
    url(r'^ajax/end/(?P<patient_id>\d+)/$', login_required(EmergencyJsonEnd.as_view(), login_url='/'), name="emergency_json_end"),
    url(r'^ajax/detail/(?P<pk>[0-9]+)/$', login_required(EmergencyJSONView.as_view(), login_url='/'), name="emergency_json_detail"),
    url(r'^ajax/patient/(?P<patient_id>[0-9]+)/$', login_required(EmergencyJSONGetPatient.as_view(), login_url='/'), name="emergency_patient_json"),
]
