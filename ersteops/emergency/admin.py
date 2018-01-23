# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import (Emergency, AttentionKind, AttentionZone, AttentionHospital,
	AttentionDerivation, ServiceCategory)

def update_is_active(EmergencyAdmin, request, queryset):
    # action fuction to help change to plan to users
    for emergency in queryset:
        emergency.is_active = True
        emergency.save()

update_is_active.short_description = "Cambiar Emergencias a estado Activo"

def update_non_active(EmergencyAdmin, request, queryset):
    # action fuction to help change to plan to users
    for emergency in queryset:
        emergency.is_active = False
        emergency.save()

update_non_active.short_description = "Cambiar Emergencias a estado Inactivo"


class EmergencyAdmin(admin.ModelAdmin):
    ''' Custom Emergency Admin Panel '''
    list_display = ("id", "odoo_client","patient_name", "grade_type", "zone", "created_at", "is_active", )
    list_filter = ("id", "odoo_client", "grade_type", "zone", "is_active", )
    search_fields = ('odoo_client', 'patient_name', )

    actions = [update_is_active, update_non_active]


admin.site.register(Emergency, EmergencyAdmin)
admin.site.register(AttentionKind)
admin.site.register(AttentionZone)
admin.site.register(AttentionHospital)
admin.site.register(AttentionDerivation)
admin.site.register(ServiceCategory)
