from django.conf.urls import url
# Use login.
from django.contrib.auth.decorators import login_required
from . import views
#from reports.views import Dashbord
from .views import UploadSymptomData, ProcessUploadSymptomData,SearchSymptomData
#from reports.views import ReportBioData, EmployeeReport

urlpatterns = [
    url(r'^upload/$', login_required(UploadSymptomData.as_view(), login_url='/login/'), name="UploadUberData"),
    url(r'^searchsymptom/$', login_required(SearchSymptomData.as_view(), login_url='/login/'), name="searchsymptom"),    
    url(r'^upload/(?P<data_id>\d+)/$', login_required(ProcessUploadSymptomData.as_view(), login_url='/login/'), name="ProcessUploadUberData"),
]
