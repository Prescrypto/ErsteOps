# log/urls.py
from django.conf.urls import url
from . import views
# Use login.
from django.contrib.auth.decorators import login_required
#from petfile.views import AddPetFileVisit, PetFileVisitList, PetFileVisitReview, PetFileVisitDetail
from printpdf.views import document_as_pdf, document_as_pdf_print
# We are adding a URL called /home
urlpatterns = [
    #url(r'^$', login_required(AddPetFileVisit.as_view(), login_url='/login/'), name="agregar consulta"),
    #url(r'^review/$',login_required(PetFileVisitList.as_view(), login_url='/login/'), name="petfilevisit"),
    #url(r'^review/(?P<pk>[0-9]+)/$',login_required(PetFileVisitReview.as_view(), login_url='/login/'), name="petfilevisitdetail"),
    #url(r'^petfile/(?P<pk>[0-9]+)/$',login_required(PetFileVisitDetail.as_view(), login_url='/login/'), name="petfilevisitdetail"),
    #url(r'^(?P<pk>[0-9]+)/$', login_required(document_as_pdf), name='pdf-generate'),
    url(r'^(?P<pk>[0-9]+)/$', login_required(document_as_pdf), name='pdf-generate'),
	url(r'^(?P<pk>[0-9]+)/print/$', login_required(document_as_pdf_print), name='pdf-print-generate'),
]