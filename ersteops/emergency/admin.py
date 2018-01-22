# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import (Emergency, AttentionKind, AttentionZone, AttentionHospital,
	AttentionDerivation, ServiceCategory)


class EmergencyAdmin(admin.ModelAdmin):
    ''' Custom Emergency Admin Panel '''
    list_display = ("id", "odoo_client", "grade_type", "zone", "created_at", "is_active", )
    list_filter = ("id", "odoo_client", "grade_type", "zone", "is_active", )


admin.site.register(Emergency, EmergencyAdmin)
admin.site.register(AttentionKind)
admin.site.register(AttentionZone)
admin.site.register(AttentionHospital)
admin.site.register(AttentionDerivation)
admin.site.register(ServiceCategory)
