from django.db import models
#from unit.models import Unit

# Create your models here.

class MedicalReport(models.Model):
    GENDER = (
        ("Masculino","Masculino"),
        ("Femenino","Femenino"),
        )
    ATENTION_PLACE = (
        ("Hogar","Hogar"),
        ("Escuela/Trabajo","Escuela/Trabajo"),
        ("Ins.deportivas","Ins.deportivas"),
        ("Ins. de recreacion","Ins. de recreacion"),
        ("Via Publica","Via Publica"),
        ("Otro","Otro"),
        )
    SERVICE_TYPE =(
        ("Traslado","Traslado"),
        ("Urgencias","Urgencias"),
        ("Cuidados Intensivos","Cuidados Intensivos"),
        ("Consulta Medica","Consulta Medica"),
        )
    CONSULTATION_REASON = (
        ("Cefalea","Cefalea"),
        ("Síncope","Síncope"),
        ("Inconciencia","Inconciencia"),
        ("Dolor Torácico","Dolor Torácico"),
        ("Otalgia","Otalgia"),
        ("Disfagia / odinofagia","Disfagia / odinofagia"),
        ("Disnea","Disnea"),
        ("Dolor Abdominal","Dolor Abdominal"),
        ("Fiebre","Fiebre"),
        ("Otros","Otros"),
        )
    EVENT_TYPE = (
        ("No Traumaticos","No Traumaticos"),
        ("Traumaticos","Traumaticos"),
        )
    TRAUMATICS = (
        ("Craneal","Craneal"),
        ("Craneoencefalico","Craneoencefalico"),
        ("Facial","Facial"),
        ("Cuello","Cuello"),
        ("Tórax","Tórax"),
        ("Abdomen","Abdomen"),
        ("Extremidades","Extremidades"),
        ("Columna vertebral","Columna vertebral"),
        ("Genitales","Genitales"),
        ("Otros","Otros"),
        )
    AIRWAY = (
        ("Ninguno","Ninguno"),
        ("Manual","Manual"),
        ("Orofaringea","Orofaringea"),
        ("Endotraqueal","Endotraqueal"),
        ("Nasofaringea","Nasofaringea"),
        ("Ventilador","Ventilador"),
        ("Aspiracion","Aspiracion"),
        ("P.N l/min","P.N l/min"),
        ("M","M"),
        )
    PUPIL_STATE = (
        ("Isocoria","Isocoria"),
        ("Midriasis","Midriasis"),
        ("Miosis","Miosis"),
        ("Anisocoria","Anisocoria"),
        )
    IMMOBILIZATION = (
        ("Columna Cervical","Columna Cervical"),
        ("Columna Torácica","Columna Torácica"),
        ("Columna Lumbar","Columna Lumbar"),
        )
    service_code = models.CharField("Codigo de Servicio",max_length=10)
    # Units m2m relation
    # Paient Data
    patient_name = models.CharField('Nombre del Paciente', max_length=255, default='')
    patient_gender = models.CharField('genero', max_length=9, default= '', blank=True, choices=GENDER)
    patient_age = models.IntegerField('edad (años)', default=0, blank=True)
    patient_affiliations = models.CharField("Filiacion",max_length=50,blank=True)
    patient_unknow = models.CharField("Paciente Desconocido",max_length=50,blank=True)
    patient_clothes = models.CharField("Vestimenta", max_length=50,blank=True)
    attention_place = models.CharField('Sitio de Atencion', max_length=9, default= '', blank=True, choices=ATENTION_PLACE)
    skin_color = models.CharField("Coloración de piel", max_length=50, default= '', blank=True,)
    service_type = models.CharField('Tipo de Servicio', max_length=9, default= '', blank=True, choices=SERVICE_TYPE)
    consultation_reason = models.CharField('Motivo de la Consulta', max_length=20, default= '', blank=True, choices=CONSULTATION_REASON)
    event_type = models.CharField('Motivo de la Consulta', max_length=20, default= '', blank=True, choices=EVENT_TYPE)
    traumatics = models.CharField('Motivo de la Consulta', max_length=20, default= '', blank=True, choices=TRAUMATICS)
    airway = models.CharField('Motivo de la Consulta', max_length=20, default= '', blank=True, choices=AIRWAY)
    # (physical_exploration = pe)
    pe_time = models.DateTimeField("Dia/Hora",blank= True)
    pe_heart_rate = models.CharField("Frequencia Cardiaca", max_length=20,default='', blank=True)
    pe_respiratory_rate = models.CharField("Frequencia Respiratoria", max_length=20,default='', blank=True)
    pe_blood_pressure = models.CharField("Presion Arterial", max_length=20,default='', blank=True)
    pe_temperature = models.CharField("Temperature", max_length=20,default='', blank=True)
    pe_oxygen_saturation = models.CharField("Saturacion O2", max_length=20,default='', blank=True)
    pe_glucometry = models.CharField("Glucometria", max_length=20,default='', blank=True)
    pe_glassgow = models.CharField("Glassgow", max_length=20,default='', blank=True)
    normal_head = models.BooleanField("Cabeza", blank=True, default=False)
    normal_face = models.BooleanField("Face", blank=True, default=False)
    normal_torax = models.BooleanField("Tórax", blank=True, default=False)
    normal_abdomen = models.BooleanField("Abdomen", blank=True, default=False)
    normal_limbs = models.BooleanField("Extremidades", blank=True, default=False)
    normal_genitals = models.BooleanField("Genitales", blank=True, default=False)
    normal_spine = models.BooleanField("Columna Vertebral", blank=True, default=False)

    # blood_products_solution 
    # Datetie utils
    created_at = models.DateTimeField("Fecha de alta",auto_now_add=True,editable=False)
    last_modified = models.DateTimeField("Última modificación",auto_now=True,editable=False)

    class Meta:
        verbose_name_plural = "Parte Medico"
        ordering = ['created_at']

    # Returns a verbose name - adjusted for Python3
    def __str__(self):
        return "{}, {}, {}".format(unicodedata.normalize('NFKD', self.odoo_client), unicodedata.normalize('NFKD', self.patient_name), self.created_at)

