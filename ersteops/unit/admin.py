from django.contrib import admin
from .models import Unit

class UnitAdmin(admin.ModelAdmin):
    ''' Customize Unit Admin '''
    pass

admin.site.register(Unit, UnitAdmin)
