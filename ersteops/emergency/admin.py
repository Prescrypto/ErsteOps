# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

# Register your models here.
from .models import (Emergency, AttentionKind, AttentionZone, AttentionHospital,
	AttentionDerivation, ServiceCategory, EmergencyDerivation)

from paperless.models import (MedicalReport)

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
    list_display = ("id","odoo_client", "erste_code", "patient_name", "grade_type", "zone", "created_at", "is_active", )
    list_filter = (
                "id","odoo_client", "erste_code",  "grade_type", "zone", "is_active",
                ('start_time', DateRangeFilter),
    )
    search_fields = ('odoo_client', 'patient_name', )
    ordering = ('-start_time',)

    fieldsets = (
        ('Paciente', {
            'fields': ( 'odoo_client', 
                        'erste_code',
                        'has_paid', 
                        'partner_name', 
                        'partner_legalname',
                        'patient_name', 
                        'patient_gender', 
                        'patient_age',
                        'is_active', 
                        'copago_amount',
                        'caller_name', 
                        'caller_relation',
                        'tel_local',
                        'tel_mobile', 
                        'subscription_type',
                        'tree_selection',
                        'service_category', 
                        'grade_type', 
                        'zone',
                        'main_complaint', 
                        'complaint_description',
                        'patient_allergies', 
                        'patient_illnesses', 
                        'attention_final_grade',
                        'attention_justification', 
                        'patient_notes',)
        }),
        ('Direccion', {
            'classes': ('collapse',),
            'fields': ( 'address_street',
                        'address_extra', 
                        'address_zip_code', 
                        'address_county',
                        'address_col',
                        'address_between', 
                        'address_and_street', 
                        'address_ref',
                        'address_front', 
                        'address_instructions',
                        'address_notes',)
        }),
        ('Unidades', {
            'classes': ('collapse',),
            'fields': ( 'units', 
                        'unit_assigned_time', 
                        #'unit_dispatched_time',
                 )
        }),
        ('Timers', {
            'classes': ('collapse',),
            'fields': ('start_time','arrival_time','derivation_time',
                    'patient_arrival','final_emergency_time')
        }),
        ('Operaciones', {
            'classes': ('collapse',),
            'fields': ('operation_notes','sales_rep')

        }),
        ('Derivaciones', {
            'classes': ('collapse',),
            'fields': ('derivations',)

        }),
        ('Parte Medico',{
            'classes': ('collapse,'),
            'fields': ('medical_report',)

            }),
    )

    actions = [update_is_active, update_non_active]


admin.site.register(Emergency, EmergencyAdmin)
admin.site.register(AttentionKind)
admin.site.register(AttentionZone)
admin.site.register(AttentionHospital)
#admin.site.register(AttentionDerivation)
admin.site.register(ServiceCategory)
admin.site.register(EmergencyDerivation)
admin.site.register(MedicalReport)