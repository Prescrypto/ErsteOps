# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Emergency, AttentionKind, AttentionZone

admin.site.register(Emergency)
admin.site.register(AttentionKind)
admin.site.register(AttentionZone)