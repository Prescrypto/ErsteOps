# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.db import models
from datetime import datetime
# Unicode 
import unicodedata
# Create your models here.

# Symptom type (adult or pediatric)
class SymptomType(models.Model):
    symptom_id = models.IntegerField("symptom id",primary_key=True,unique=True)
    name = models.CharField("symptom",max_length=20,default='')
    created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
    last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)

    class Meta:
        verbose_name_plural = "Symptom Type"
        ordering = ['name']

    def __str__(self):
        return self.name

class SymptomDataFile(models.Model):
  name = models.CharField("nombre de la carga",max_length=100,unique=True)
  symptom_file = models.FileField("archivo de syntomas",max_length=100,upload_to="decisiontree/symptom_files",default="")
  procesed = models.NullBooleanField("procesado")
  read_lines = models.IntegerField("Lineas leida",blank=True,default=0)
  insert_lines = models.IntegerField("Lineas Insertadas",blank=True,default=0)
  update_lines = models.IntegerField("Lineas actualizadas",blank=True,default=0)
  created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
  last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
  class Meta:
    verbose_name_plural = "Symptom Data File"
    ordering = ['created_at']
  def __str__(self):  
    return self.name

class SymptomDataDetail(models.Model):
  idx = models.CharField("idx",max_length=18,primary_key=True,unique=True)
  name = models.CharField("sintoma",max_length=200,default='')
  n1 = models.CharField('N1',max_length=3,default='')
  n2 = models.CharField('N2',max_length=3,default='')
  n3 = models.CharField('N3',max_length=3,default='')
  n4 = models.CharField('N4',max_length=3,default='')
  n5 = models.CharField('N5',max_length=3,default='')
  n6 = models.CharField('N6',max_length=3,default='')
  n7 = models.CharField('N7',max_length=3,default='')
  level = models.CharField('Nivel',max_length=2,default='')
  grade = models.CharField('Grado',max_length=50,default='')
  key = models.CharField('Clave',max_length=18,default='')
  symptom_type = models.ForeignKey(SymptomType,
    related_name="symptom_type_name",
    verbose_name= "symptom_type",
    default=3
    )
  created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
  last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
  class Meta:
    verbose_name_plural = "Symptom Data Detail"
    ordering = ['created_at']
  def __str__(self):  
    return self.idx+' - '+self.name

