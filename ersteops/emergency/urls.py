from django.conf.urls import url
from . import views
from emergency.views import EmergencyRecord

urlpatterns = [
	url(r'^$',EmergencyRecord.as_view(),name="emergencyrecord"),
]