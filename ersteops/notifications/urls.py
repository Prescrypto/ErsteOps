from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^emergency/', views.emergency),
    #url(r'^units/', views.units),
    url(r'^derivation/', views.derivation),
]