''' Urls for Home Views '''
from django.conf.urls import include, url
from .views import home, logout_page, report_view

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^logout/$', logout_page, name='logout_page'),
    url(r'^reportes/$', report_view, name='report_view'),
]
