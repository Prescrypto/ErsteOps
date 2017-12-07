# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from datetime import datetime, timedelta
from vehicle import models as models_vehicle

import json
from channels import Group
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
@python_2_unicode_compatible
class Emergency(models.Model):
    odoo_client = models.CharField("cliente id",max_length=50,unique=False)
    grade_type = models.ForeignKey("AttentionKind",
    related_name="attention_kind_name",
    verbose_name= "tipo"
        )
    zone = models.ForeignKey("AttentionZone",
    related_name="zone_name",
    verbose_name="zone"
        )
    start_time = models.DateTimeField("inicio",default=datetime.now)
    end_time = models.DateTimeField("fin",default=datetime.now,blank=True)
    is_active = models.NullBooleanField("activa")
    unit = models.ManyToManyField(models_vehicle.Unit,
        related_name="unit_name",
        verbose_name="Unidad"
    )
    created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
    last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
    class Meta:
        verbose_name_plural = "Emergency"
        ordering = ['created_at']
    def __str__(self):  
        return str(self.id)

@receiver(post_save, sender=Emergency, dispatch_uid="emergency_notifications")
def emergency_notifications(sender, instance, **kwargs):

    emergDict={}
    emergDict["odoo_client"]=instance.odoo_client
    emergDict["grade_type"]=str(instance.grade_type)
    emergDict["zone"]=str(instance.zone)
    emergDict["start_time"]=instance.start_time.strftime('%b %-d %-I:%M %p')
    emergDict["end_time"]=instance.end_time.strftime('%b %-d %-I:%M %p')
    emergDict["is_active"]=instance.is_active
    emergDict["unit"]=str(instance.unit)
    emergDict["created_at"]=instance.created_at.strftime('%b %-d %-I:%M %p')
    emergDict["last_modified"]=instance.last_modified .strftime('%b %-d %-I:%M %p')
    emergJson=json.dumps(emergDict)
    
    Group('notify-emergency').send(
            {"text": json.dumps(emergJson)}
        )
    


@python_2_unicode_compatible
class AttentionKind(models.Model):
    grade_type = models.CharField("Grado",max_length=100,unique=True,primary_key=True)
    name = models.CharField("Tipo de Consulta",max_length=100,unique=True)
    description = models.TextField("Descripcion",default="")
    created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
    last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
    class Meta:
        verbose_name_plural = "Kind of Attention"
        ordering = ['created_at']
    def __str__(self):  
        return self.grade_type + ' - ' +self.name


@python_2_unicode_compatible
class AttentionZone(models.Model):
    zone_id = models.CharField("Zona id",max_length=100,unique=True,primary_key=True)
    name = models.CharField("Descripcion",max_length=100,unique=True)
    created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
    last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
    class Meta:
        verbose_name_plural = "zone"
        ordering = ['created_at']
    def __str__(self):  
        return self.zone_id + ' - ' +self.name

