import json
import unicodedata

from django.db import models
from django.utils import timezone

from channels import Group
from django.dispatch import receiver
from django.db.models.signals import post_save

from core.utils import eventDuration


class Emergency(models.Model):
    ''' Emergency incident model '''
    GENDER = (
        ("Masculino","Masculino"),
        ("Femenino","Femenino"),
        )
    odoo_client = models.CharField("cliente id", max_length=50)
    # Service Category
    service_category=models.ForeignKey("ServiceCategory",
        related_name="service_category_name",
        verbose_name= "Tipo de emergencia",
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
    start_time = models.DateTimeField("Inicio toma de datos", default=timezone.now)
    # Records when the operator ends capture of basic emergency data
    end_time = models.DateTimeField("Fin toma de datos", default=timezone.now, blank=True)
    # Records when unit is assigned
    unit_assigned_time = models.DateTimeField("Asignacion de unidad", default=timezone.now, blank=True)
    # Records when unit is dispatched from current location to emergency address
    unit_dispatched_time = models.DateTimeField("Despacho de unidad", default=timezone.now, blank=True)
    # Records when unit arives to emergency adress
    arrival_time = models.DateTimeField("Arrivo de unidad", default=timezone.now, blank=True)
    # Records when TUM begins attention
    attention_time = models.DateTimeField("Inicio de atencion", default=timezone.now, blank=True)
    # Records when patient is derived
    derivation_time = models.DateTimeField("Inicio de derivacion", default=timezone.now, blank=True)
    # Records when unit arrive to hospital
    hospital_arrival = models.DateTimeField("Llegada hopital", default=timezone.now, blank=True)
    # Record when patient arrive to hopsital
    patient_arrival = models.DateTimeField("Paciente atencion hopital", default=timezone.now, blank=True)
    final_emergency_time = models.DateTimeField("Fin emergencia", default=timezone.now, blank=True)

    is_active = models.NullBooleanField("Activa", default=True)

    # Units m2m relation
    units = models.ManyToManyField('unit.Unit', related_name='units', blank=True)

    # Attention address
    address_street = models.CharField('Calle y numero', default='', max_length=100, blank=True)
    address_extra = models.CharField('Calle', default='', max_length=100, blank=True)
    address_zip_code = models.CharField('Codigo Postal', default='', max_length=5, blank=True)
    address_county = models.CharField('Delegacion', default='', max_length=50, blank=True)
    address_col = models.CharField('Colonia', default='', max_length=50, blank=True)
    address_between = models.CharField('entre la calle', default='', max_length=100, blank=True)
    address_and_street = models.CharField('y la calle', default='', max_length=100, blank=True)
    address_ref = models.CharField('referencias', default='', max_length=100, blank=True)
    address_front = models.CharField('fachada', default='', max_length=100, blank=True)
    address_instructions = models.CharField('Instruccciones llegada', default='', max_length=100, blank=True)
    address_notes = models.TextField('Notas', default='', blank=True)
    # Caller Data
    caller_name = models.CharField('Persona que llama', max_length=100, blank=True)
    caller_relation = models.CharField('Relacion con el paciente', max_length=50, blank=True)
    # Paient Data
    patient_name = models.CharField('Nombre del Paciente', max_length=255, default='')
    patient_gender = models.CharField('genero', max_length=9, default= '', blank=True, choices=GENDER)
    patient_age = models.IntegerField('edad (años)', default=0, blank=True)
    patient_allergies = models.CharField('alergias', max_length=100, default='', blank=True)
    patient_illnesses = models.CharField('Enfermedades diagnosticadas', max_length=100, default='', blank=True)
    patient_notes = models.TextField('Notas paciente', blank=True, default='')
    #Details of attention
    attention_final_grade = models.ForeignKey("AttentionKind",
                                            related_name="final_attention_kind_name",
                                            verbose_name= "Grado de atencion final",
                                            blank=True,
                                            null=True)
    attention_justification = models.TextField(u'Justificación', blank=True, default='')
    # Symptoms
    main_complaint = models.CharField('sintoma principal', max_length=100, default='', blank=True)
    complaint_description = models.TextField('descripcion de los sintomas', default='', blank=True)
    subscription_type = models.CharField('subscripcion', max_length=100, default='', blank=True)
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
        ''' Return name of instance '''
        return self.odoo_client


    def emergencyTimer(self):
        # Calculate emergency Timer
        return eventDuration(self.start_time,self.final_emergency_time)

    def dataTimer(self):
        # Calculate data timer
        return eventDuration(self.start_time,self.end_time)

    def unitTimer(self):
        # Calculate unit assigment timer
        return eventDuration(self.start_time,self.unit_assigned_time)

    def dispatchTimer(self):
        # Calculate Dispatch Timer
        return eventDuration(self.start_time,self.unit_dispatched_time)

    def arrivalTimer(self):
        # Calculate Arrival Timer
        return eventDuration(self.start_time,self.arrival_time)

    def attentionTimer(self):
        # Calculate Attention timer: time takes medic between arrive location and begin attend to patient
        return eventDuration(self.start_time,self.attention_time)

    def derivationTimer(self):
        # Calculate derivation timer
        return eventDuration(self.start_time,self.derivation_time)

    def hospitalTimer(self):
        # Calculate hospital timer
        return eventDuration(self.start_time,self.hospital_arrival)

    def patientTimer(self):
        # Calculate patient arrival
        return eventDuration(self.start_time,self.patient_arrival)

    def save(self, **kwargs):
        ''' Saves and checks whether the object is a candidate for notification '''

        is_new_emergency = True if self.pk is None else False

        if is_new_emergency:
            self.attention_final_grade = self.grade_type

        try:
            old_instance = False if is_new_emergency else Emergency.objects.get(pk=self.pk)
        except Emergency.DoesNotExist:
            print("check legacy")
            return

        super(Emergency, self).save(**kwargs)

        type_notif = ""
        if is_new_emergency:
            if self.is_active:
                #Is new and is active
                type_notif = "New"
        elif not self.is_active and old_instance.is_active:
            #Updated from is_active=True to is_active=False
            type_notif = "Deactivate"
        elif self.is_active and not old_instance.is_active:
            #Updated from is_active=False to is_active=True
            type_notif = "Activate"
        # elif self.is_active and old_instance.unit != self.unit:
        #     #Update units in emergency
        #     type_notif = "Unid Update" # TODO add new unit here
        elif self.is_active:
            #Update simple and is_active
            type_notif = "Update"
        else:
            #is not a candidate to notifications
            return

        emergDict = emergency_dictionary(self)
        emergDict.update({
            "type_notif" : type_notif,
            "type_data" : "Emergency",
        })
        emergJson=json.dumps(emergDict)

        print("TypeNotification: {}".format(type_notif))
        Group('notifications').send({
            "text": json.dumps(emergJson),
        })

    # Returns a verbose name - adjusted for Python3
    def __str__(self):
        return "{}, {}, {}".format(unicodedata.normalize('NFKD', self.odoo_client), unicodedata.normalize('NFKD', self.patient_name), self.created_at)


def emergency_dictionary(instance):

    units=[]
    for unit in instance.units.all():
        continue
        _unit_json = {
            # TODO add fields of UNIT
        }
        units.append(_unit_json)

    emergDict={
        "pk":instance.pk,
        "id":instance.pk,
        "odoo_client":instance.odoo_client,
        "grade_type":str(instance.grade_type),
        "zone":str(instance.zone),

        "unit":units,

        "start_time":instance.start_time.isoformat(),
        "end_time":instance.end_time.isoformat(),
        "created_at":instance.created_at.isoformat(),
        "last_modified":instance.last_modified.isoformat(),
        "unit_assigned_time":instance.unit_assigned_time.isoformat(),
        "unit_dispatched_time":instance.unit_dispatched_time.isoformat(),
        "arrival_time":instance.arrival_time.isoformat(),
        "attention_time":instance.attention_time.isoformat(),
        "derivation_time":instance.derivation_time.isoformat(),
        "hospital_arrival":instance.hospital_arrival.isoformat(),
        "patient_arrival":instance.patient_arrival.isoformat(),
        "final_emergency_time":instance.final_emergency_time.isoformat(),

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


class AttentionKind(models.Model):
    ''' Attention Kind Model can be G1, G2, G3 '''
    grade_type = models.CharField("Grado", max_length=100,unique=True,primary_key=True)
    name = models.CharField("Tipo de Consulta", max_length=100,unique=True)
    description = models.TextField("Descripcion", default="")

    #
    created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
    last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)

    class Meta:
        verbose_name_plural = "Tipo de Atención"
        ordering = ['created_at']

    def __str__(self):
        return self.grade_type + ' - ' +self.name


class AttentionZone(models.Model):
    ''' Zona de Atención '''
    zone_id = models.CharField("Zona id", max_length=100,unique=True,primary_key=True)
    name = models.CharField("Descripcion", max_length=100,unique=True)

    # Datetime utils
    created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
    last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)

    class Meta:
        verbose_name_plural = "Zona"
        ordering = ['created_at']

    def __str__(self):
        return self.zone_id + ' - ' +self.name


class AttentionHospital(models.Model):
    ''' Hospital Model for Derivation cases'''
    name = models.CharField("hospital", max_length=100,unique=True)
    address = models.TextField("direccion", max_length=100, blank=True)
    phone = models.CharField("telefono", max_length=15, default='', blank=True)

    # Datetime utils
    created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
    last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)

    class Meta:
        verbose_name_plural = "Hospital"
        ordering = ['name']

    def __str__(self):
        return self.name


class AttentionDerivation(models.Model):
    '''  Service Derivation model'''
    emergency = models.ForeignKey('Emergency',
        related_name = "derivation_emergency_name",
        verbose_name = "emergencia",
        default=1,
        )
    motive = models.CharField("Motivo", max_length=100, blank=True)
    hospital = models.ForeignKey("AttentionHospital",
    related_name="attention_hospital_name",
    verbose_name= "hospital"
        )
    eventualities = models.TextField("eventualidades", max_length=100, blank=True)
    reception = models.CharField("quien recibe en hospital", max_length=100, blank=True)
    notes = models.TextField("notas", max_length=100, blank=True)

    # Datetime utils
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
        "created_at" : instance.created_at.isoformat(),
        "last_modified" : instance.last_modified.isoformat()
    }

    return derivDict


class ServiceCategory(models.Model):
    ''' Model of Service Category '''

    name = models.CharField("Categoria", max_length=100, unique=True)
    description = models.TextField("Descripcion", blank=True)

    # Datetime utils
    created_at = models.DateTimeField("Fecha de alta", auto_now_add=True, editable=False)
    last_modified = models.DateTimeField("Ultima modificacion", auto_now=True, editable=False)

    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name
