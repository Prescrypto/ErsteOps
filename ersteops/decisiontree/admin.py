from django.contrib import admin
#from __future__ import unicode_literals
from django.contrib import admin
from .models import SymptomType,SymptomDataFile,SymptomDataDetail

# Register your models here.
admin.site.register(SymptomType)
admin.site.register(SymptomDataFile)
admin.site.register(SymptomDataDetail)

#=CONCATENATE(B2,C2,D2,E2,F2,G2,H2)