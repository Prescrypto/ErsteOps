# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mptt.admin import MPTTModelAdmin

# Register your models here.
from .models import (Emergency, AttentionKind, AttentionZone, AttentionHospital,
	AttentionDerivation, Symptom)


admin.site.register(Emergency)
admin.site.register(AttentionKind)
admin.site.register(AttentionZone)
admin.site.register(AttentionHospital)
admin.site.register(AttentionDerivation)

admin.site.register(Symptom, MPTTModelAdmin)
