from django.conf.urls import url
from . import views
from emergency.views import EmergencyBlank, EmergencyNew, EmergencyListView, EmergencyDetailView, EmergencyDashbordList, EmergencyDerivation, EmergencyUpdate, EmergencyClientOdoo, EmergencyClientModal,EmergencyNewModal, EmergencyGetPatient

urlpatterns = [
    url(r'^$',EmergencyBlank.as_view(),name="emergencyblank"),
    url(r'^new/$',EmergencyNew.as_view(),name="emergencynew"),
    url(r'^list/$',EmergencyListView.as_view(),name="emergencylist"),
    url(r'^modal/$',EmergencyClientModal.as_view(),name="odoomodal"),
    url(r'^newmodal/$',EmergencyNewModal.as_view(),name="newincidentmodal"),
    url(r'^odooapi/$',EmergencyClientOdoo.as_view(),name="emergencyodoo"),
    url(r'^update/(?P<pk>[0-9]+)/$',EmergencyUpdate.as_view(),name="emergencyupdate"),
    url(r'^dashboard/$',EmergencyDashbordList.as_view(),name="emergencydashbord"),
    url(r'^derivation/$',EmergencyDerivation.as_view(),name="emergencyderivation"),
    url(r'^(?P<pk>[0-9]+)/$', EmergencyDetailView.as_view(), name='emergencydetail'),
    url(r'^getpatient/(?P<patient_id>\d+)/$', EmergencyGetPatient.as_view(), name='emergencyeeteatient'),
]
