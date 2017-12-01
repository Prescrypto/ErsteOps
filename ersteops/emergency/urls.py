from django.conf.urls import url
from . import views
from emergency.views import EmergencyBlank, EmergencyNew, EmergencyListView, EmergencyDetailView, EmergencyDashbordList, EmergencyOdo

urlpatterns = [
	url(r'^$',EmergencyBlank.as_view(),name="emergencyblank"),
	url(r'^new/$',EmergencyNew.as_view(),name="emergencynew"),
	url(r'^listodoo/$',EmergencyOdo.as_view(),name="emergencynew"),
	url(r'^list/$',EmergencyListView.as_view(),name="emergencylist"),
	url(r'^dashbord/$',EmergencyDashbordList.as_view(),name="emergencydashbord"),
	url(r'^(?P<pk>[0-9]+)/$', EmergencyDetailView.as_view(), name='emergencydetail'),
]
