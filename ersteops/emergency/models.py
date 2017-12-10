# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from datetime import datetime, timedelta
from vehicle import models as models_vehicle

from core.utils import eventDuration
# Create your models here.

#Emergency incident table
@python_2_unicode_compatible
class Emergency(models.Model):
    GENDER = (
        ("Masculino","Masculino"),
        ("Femenino","Femenino"),
        )
    odoo_client = models.CharField("cliente id",max_length=50,unique=False)
    # Triage
    grade_type = models.ForeignKey("AttentionKind",
    related_name="attention_kind_name",
    verbose_name= "tipo"
        )
    zone = models.ForeignKey("AttentionZone",
    related_name="zone_name",
    verbose_name="zone"
        )
    # Timers
    # Emergency statrt an end time: when the operator select new incident
    # Initial call time
    start_time = models.DateTimeField("inicio toma de datos",default=datetime.now)
    # Records when the operator ends capture of basic emergency data
    end_time = models.DateTimeField("fin toma de datos",default=datetime.now,blank=True)
    # Records when unit is assigned
    unit_assigned_time = models.DateTimeField("asignacion de unidad",default=datetime.now,blank=True)
    # Records when unit is dispatched from current location to emergency address
    unit_dispatched_time = models.DateTimeField("despacho de unidad",default=datetime.now,blank=True)
    # Records when unit arives to emergency adress
    arrival_time = models.DateTimeField("arrivo de unidad",default=datetime.now,blank=True)
    # Records when TUM begins attention
    attention_time = models.DateTimeField("inicio de atencion",default=datetime.now,blank=True)
    # Records when patient is derived
    derivation_time = models.DateTimeField("inicio de derivacion",default=datetime.now,blank=True)
    # Records when unit arrive to hospital
    hospital_arrival = models.DateTimeField("llegada hopital",default=datetime.now,blank=True)
    # Record when patient arrive to hopsital
    patient_arrival = models.DateTimeField("paciente atencion hopital",default=datetime.now,blank=True)
    final_emergency_time = models.DateTimeField("fin emergencia",default=datetime.now,blank=True)
    is_active = models.NullBooleanField("activa")
    unit = models.ManyToManyField(models_vehicle.Unit,
        related_name="unit_name",
        verbose_name="Unidad",
        blank=True,
    )
    # Attention address
    address_street = models.CharField('Calle y numero',default='', max_length=100,blank=True)
    address_extra = models.CharField('Calle',default='',max_length=100,blank=True)
    address_zip_code = models.CharField('Codigo Postal',default='',max_length=5,blank=True)
    address_county = models.CharField('Delegacion',default='',max_length=50,blank=True)
    address_col = models.CharField('Colonia',default='',max_length=50,blank=True)
    address_between = models.CharField('entre la calle',default='',max_length=100,blank=True)
    address_and_street = models.CharField('y la calle',default='',max_length=100,blank=True)
    address_ref = models.CharField('referencias',default='',max_length=100,blank=True)
    address_front = models.CharField('fachada',default='',max_length=100,blank=True)
    address_instructions = models.CharField('Instruccciones llegada',default='',max_length=100, blank=True)
    address_notes = models.TextField('Notas',default='',blank=True)
    # Caller Data
    caller_name = models.CharField('Persona que llama',max_length=100,blank=True)
    caller_relation = models.CharField('Relacion con el paciente',max_length=50,blank=True)
    # Paient Data
    patient_gender = models.CharField('genero',max_length=9,default= '',blank=True,choices = GENDER)
    patient_age = models.IntegerField('edad',default=0,blank=True)
    patient_allergies = models.CharField('alergias',max_length=100,default='',blank=True)
    patient_illnesses = models.CharField('Enfermedades diagnosticadas',max_length=100,default='',blank=True)
    patient_notes = models.TextField('Notas paciente',blank=True,default='')
    # Symptoms
    main_complaint = models.CharField('sintoma principal',max_length=100,default='',blank=True)
    complaint_descriprion = models.TextField('descripcion de los sintomas',default='',blank=True)
    required_attention = models.CharField('Tipo de atencion requerida',default='',max_length=100,blank=True)
    subscription_type = models.CharField('subscripcion',max_length=100,default='',blank=True)
    # derivation = models.ManyToManyField('AttentionDerivation',
    #     related_name = 'derivation_issue',
    #     verbose_name = 'Derivacion',
    #     blank=True,
    #     )
    created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
    last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
    class Meta:
        verbose_name_plural = "Emergency"
        ordering = ['created_at']
    def __str__(self):  
        return str(self.id)
    # Emergency Timer
    def emergencyTimer(self):
        # Calculate emergency Timer
        return eventDuration(self.start_time,self.final_emergency_time)
    # data Timer
    def dataTimer(self):
        # Calculate data timer
        return eventDuration(self.start_time,self.end_time)
    # Unit Timer
    def unitTimer(self):
        # Calculate unit assigment timer
        return eventDuration(self.start_time,self.unit_assigned_time)
    # Dispatch Timer
    def dispatchTimer(self):
        # Calculate Dispatch Timer
        return eventDuration(self.start_time,self.unit_dispatched_time)
    #Arrival Timer
    def arrivalTimer(self):
        # Calculate Arrival Timer
        return eventDuration(self.start_time,self.arrival_time)
    # Attention timer
    def attentionTimer(self):
        # Calculate Attention timer: time takes medic between arrive location and begin attend to patient
        return eventDuration(self.start_time,self.attention_time)
    # Derivation Timer
    def derivationTimer(self):
        # Calculate derivation timer
        return eventDuration(self.start_time,self.derivation_time)
    # Hospital timer
    def hospitalTimer(self):
        # Calculate hospital timer
        return eventDuration(self.start_time,self.hospital_arrival)
    # Patient arival
    def patientTimer(self):
        # Calculate patient arrival
        return eventDuration(self.start_time,self.patient_arrival)

# Emergency attention grade G1,G2,G3, etc.(Triage)
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

# Emergency attention zone
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

# Hospital model
@python_2_unicode_compatible
class AttentionHospital(models.Model):
    name = models.CharField("hospital",max_length=100,unique=True)
    address = models.TextField("direccion",max_length=100,blank=True)
    phone = models.CharField("telefono",max_length=15,default='',blank=True)
    created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
    last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
    class Meta:
        verbose_name_plural = "Hospital"
        ordering = ['name']
    def __str__(self):  
        return self.name

# Hospital
@python_2_unicode_compatible
class AttentionDerivation(models.Model):
    emergency = models.ForeignKey('Emergency',
        related_name = "derivation_emergency_name",
        verbose_name = "emergencia",
        default=1,
        )
    motive = models.CharField("Motivo",max_length=100,blank=True)
    hospital = models.ForeignKey("AttentionHospital",
    related_name="attention_hospital_name",
    verbose_name= "hospital"
        )
    eventualities = models.TextField("eventualidades",max_length=100,blank=True)
    reception = models.CharField("quien recibe en hospital",max_length=100,blank=True)
    notes = models.TextField("notas",max_length=100,blank=True)
    created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
    last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
    class Meta:
        verbose_name_plural = "Derivacion"
        ordering = ['created_at']
    def __str__(self):  
        return self.motive


