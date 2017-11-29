from django.conf.urls import url
from . import views
from emergency.views import EmergencyBlank, EmergencyNew, EmergencyListView

urlpatterns = [
	url(r'^$',EmergencyBlank.as_view(),name="emergencyblank"),
	url(r'^new/$',EmergencyNew.as_view(),name="emergencynew"),
	url(r'^list/$',EmergencyListView.as_view(),name="emergencylist"),
]