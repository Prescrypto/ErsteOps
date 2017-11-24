from django.contrib import admin

# Register your models here.
from .models import Unit, Brand, UnitType

admin.site.register(Unit)
admin.site.register(Brand)
admin.site.register(UnitType)