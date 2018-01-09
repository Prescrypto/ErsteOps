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

from core.utils import eventDuration
# Create your models here.


@python_2_unicode_compatible
class Emergency(models.Model):
    ''' Emergency incident model '''
    GENDER = (
        ("Masculino","Masculino"),
        ("Femenino","Femenino"),
        )
    odoo_client = models.CharField("cliente id",max_length=50,unique=False)
    # Service Category
    service_category=models.ForeignKey("ServiceCategory",
        related_name="service_category_name",
        verbose_name= "Tipo de emergencia",
        #default=1,
        blank=True,
        null=True
        )
    # Triage
    grade_type = models.ForeignKey("AttentionKind",
    related_name="attention_kind_name",
    verbose_name= "Grado Emergencia"
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
    patient_name = models.CharField('Nombre del Paciente',max_length=255, default='')
    patient_gender = models.CharField('genero',max_length=9,default= '',blank=True,choices = GENDER)
    patient_age = models.IntegerField('edad (años)',default=0,blank=True)
    patient_allergies = models.CharField('alergias',max_length=100,default='',blank=True)
    patient_illnesses = models.CharField('Enfermedades diagnosticadas',max_length=100,default='',blank=True)
    patient_notes = models.TextField('Notas paciente',blank=True,default='')
    #Details of attention
    attention_final_grade = models.ForeignKey("AttentionKind",
    related_name="final_attention_kind_name",
    verbose_name= "Grado de atencion final",
    blank=True,
    null=True
        )
    attention_justification = models.TextField(u'Justificación',blank=True,default='')
    # Symptoms
    main_complaint = models.CharField('sintoma principal',max_length=100,default='',blank=True)
    complaint_descriprion = models.TextField('descripcion de los sintomas',default='',blank=True)
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
    def save(self, **kwargs):
        #Saves and checks whether the object is a candidate for notification
        #new object
        newEmerg=True if self.pk is None else False
        if newEmerg:
            self.attention_final_grade=self.grade_type

        try:
            old_instance=False if newEmerg else Emergency.objects.get(pk=self.pk)
        except Emergency.DoesNotExist:
            return

        super(Emergency, self).save(**kwargs)

        type_notif=""
        if newEmerg:
            if self.is_active:
                #Is new and is active
                type_notif="New"
        elif not self.is_active and old_instance.is_active:
            #Updated from is_active=True to is_active=False
            type_notif="Deactivate"
        elif self.is_active and not old_instance.is_active:
            #Updated from is_active=False to is_active=True
            type_notif="Activate"
        elif self.is_active and old_instance.unit != self.unit:
            #Update units in emergency
            type_notif="Unid Update"
        elif self.is_active:
            #Update simple and is_active
            type_notif="Update"
        else:
            #is not a candidate to notifications
            return

        emergDict=emergency_dictionary(self)
        emergDict["type_notif"]=type_notif
        emergDict["type_data"]="Emergency"
        emergJson=json.dumps(emergDict)


        Group('notifications').send(
                {"text": json.dumps(emergJson)}
            )


def emergency_dictionary(instance):

    units=[]
    for unit in instance.unit.all():
        unitDict={
            "pk":unit.pk,
            "unit_id":unit.unit_id,
            "model":unit.model,
            "year":unit.year,
            "license_plate":unit.license_plate,
            "brand":str(unit.brand),
            "unit_type":str(unit.unit_type),
            "is_active":unit.is_active,
            "assigned":unit.assigned,
            "created_at":unit.created_at.strftime('%b %-d %-I:%M %p'),
            "last_modified":unit.last_modified.strftime('%b %-d %-I:%M %p'),
        }
        units.append(unitDict)
    emergDict={
        "pk":instance.pk,
        "odoo_client":instance.odoo_client,
        "grade_type":str(instance.grade_type),
        "zone":str(instance.zone),

        "unit":units,

        "start_time":instance.start_time.strftime('%b %-d %-I:%M %p'),
        "end_time":instance.end_time.strftime('%b %-d %-I:%M %p'),
        "created_at":instance.created_at.strftime('%b %-d %-I:%M %p'),
        "last_modified":instance.last_modified.strftime('%b %-d %-I:%M %p'),
        "unit_assigned_time":instance.unit_assigned_time.strftime('%b %-d %-I:%M %p'),
        "unit_dispatched_time":instance.unit_dispatched_time.strftime('%b %-d %-I:%M %p'),
        "arrival_time":instance.arrival_time.strftime('%b %-d %-I:%M %p'),
        "attention_time":instance.attention_time.strftime('%b %-d %-I:%M %p'),
        "derivation_time":instance.derivation_time.strftime('%b %-d %-I:%M %p'),
        "hospital_arrival":instance.hospital_arrival.strftime('%b %-d %-I:%M %p'),
        "patient_arrival":instance.patient_arrival.strftime('%b %-d %-I:%M %p'),
        "final_emergency_time":instance.final_emergency_time.strftime('%b %-d %-I:%M %p'),

        "is_active":instance.is_active,
        "address_street":instance.address_street,
        "address_extra":instance.address_extra,
        "address_zip_code":instance.address_zip_code,
        "address_county":instance.address_county,
        "address_col":instance.address_col,
        "address_between":instance.address_between,
        "address_and_street":instance.address_and_street,
        "address_ref":instance.address_ref,
        "address_front":instance.address_front,
        "address_instructions":instance.address_instructions,
        "address_notes":instance.address_notes,
        "caller_name":instance.caller_name,
        "caller_relation":instance.caller_relation,
        "patient_name":instance.patient_name,
        "patient_allergies":instance.patient_allergies,
        "patient_illnesses":instance.patient_illnesses,
        "patient_notes":instance.patient_notes,
        "attention_final_grade":str(instance.attention_final_grade),
        "attention_justification":instance.attention_justification,
        "main_complaint":instance.main_complaint,
        "complaint_descriprion":instance.complaint_descriprion,
        "subscription_type":instance.subscription_type,
    }

    return emergDict





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

    def save(self, **kwargs):
        newDerivation=True if self.pk is None else False

        super(AttentionDerivation, self).save(**kwargs)

        type_notif=""
        if newDerivation:
            type_notif="New"
        else:
            type_notif="Update"

        derivDict=derivation_dictionary(self)
        derivDict["type_notif"]=type_notif
        derivDict["type_data"]="Derivation"

        derivJson=json.dumps(derivDict)

        Group('notifications').send(
                {"text": json.dumps(derivJson)}
            )

def derivation_dictionary(instance):
    derivDict={
        "pk" : instance.pk,
        "emergency" : str(instance.emergency),
        "motive" : instance.motive,
        "hospital" : str(instance.hospital),
        "eventualities" : instance.eventualities,
        "reception" : instance.reception,
        "notes" : instance.notes,
        "created_at" : instance.created_at.strftime('%b %-d %-I:%M %p'),
        "last_modified" : instance.last_modified.strftime('%b %-d %-I:%M %p')
    }

    return derivDict


# service_category
@python_2_unicode_compatible
class ServiceCategory(models.Model):
    name = models.CharField("Categoria", max_length=100, unique=True)
    description = models.TextField("Descripcion", blank=True)
    created_at = models.DateTimeField("Fecha de alta", auto_now_add=True, editable=False)
    last_modified = models.DateTimeField("Ultima modificacion", auto_now=True, editable=False)
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name

#class EmergencyType(models.Model):
