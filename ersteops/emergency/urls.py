from django.conf.urls import url
from . import views
from emergency.views import EmergencyBlank, EmergencyNew, EmergencyListView, EmergencyDetailView, EmergencyDashbordList, EmergencyDerivation, EmergencyUpdate

urlpatterns = [
    url(r'^$',EmergencyBlank.as_view(),name="emergencyblank"),
    url(r'^new/$',EmergencyNew.as_view(),name="emergencynew"),
    url(r'^list/$',EmergencyListView.as_view(),name="emergencylist"),
    url(r'^update/(?P<pk>[0-9]+)/$',EmergencyUpdate.as_view(),name="emergencyupdate"),
    url(r'^dashbord/$',EmergencyDashbordList.as_view(),name="emergencydashbord"),
    url(r'^derivation/$',EmergencyDerivation.as_view(),name="emergencyderivation"),
    url(r'^(?P<pk>[0-9]+)/$', EmergencyDetailView.as_view(), name='emergencydetail'),
]
