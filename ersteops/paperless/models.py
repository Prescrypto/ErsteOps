from django.db import models
#from unit.models import Unit
from django.contrib.auth.models import User
import unicodedata
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
    YES_NO = (
        ('Si','Si'),
        ('No','No'),
        )
    DERIVATION =  (
        ('Si','Si'),
        ('No','No'),
        ('Hogar','Hogar'),
        ('Hospital','Hospital'),
        ('Otro','Otro'),
        )
    HEALTH_STATE = (
        ('Delicado','Delicado'),
        ('Grave','Grave'),
        ('Muy Grave','Muy Grave'),
        )
    odoo_client = models.CharField("Cliente id(Legacy)", max_length=50,default ='',)
    erste_code = models.CharField("ID Code", max_length=50, blank=True, default="")
    service_code = models.CharField("Codigo de Servicio",max_length=10,default='')
    service_unit = models.CharField("Unidad Movil",max_length=10,default='')
    service_unit_type = models.CharField("Tipo Unidad",max_length=50,default='')
    service_unit_plate = models.CharField("No.Placas",max_length=10,default='')
    # Units m2m relation
    # Paient Data
    service_geo_lat = models.CharField('Latitud',max_length=15, blank=True ,default='')
    service_geo_lon = models.CharField('Longitud', max_length=15,  blank=True, default='')
    patient_name = models.CharField('Nombre del Paciente', max_length=255, default='')
    patient_gender = models.CharField('genero', max_length=9, default= '', blank=True, choices=GENDER)
    patient_age = models.IntegerField('edad (años)', default=0, blank=True)
    patient_affiliations = models.CharField("Filiacion",max_length=50,blank=True)
    patient_unknow = models.CharField("Paciente Desconocido",max_length=50,blank=True)
    patient_clothes = models.CharField("Vestimenta", max_length=50,blank=True)
    patient_phone = models.CharField("Telefono:", max_length=15,blank=True ,default='')
    attention_place = models.CharField('Sitio de Atencion', max_length=9, default= '', blank=True, choices=ATENTION_PLACE)
    skin_color = models.CharField("Coloración de piel", max_length=50, default= '', blank=True,)
    service_type = models.CharField('Tipo de Servicio', max_length=9, default= '', blank=True, choices=SERVICE_TYPE)
    consultation_reason = models.CharField('Motivo de la Consulta', max_length=20, default= '', blank=True, choices=CONSULTATION_REASON)
    event_type = models.CharField('Tipo de Evento', max_length=20, default= '', blank=True, choices=EVENT_TYPE)
    traumatics = models.CharField('Traumatico', max_length=20, default= '', blank=True, choices=TRAUMATICS)
    airway = models.CharField('Via Aerea', max_length=20, default= '', blank=True, choices=AIRWAY)
    # (physical_exploration = pe)
    pe_time = models.DateTimeField("Dia/Hora",blank= True, null =True)
    pe_heart_rate = models.CharField("Frequencia Cardiaca", max_length=20,default='', blank=True)
    pe_respiratory_rate = models.CharField("Frequencia Respiratoria", max_length=20,default='', blank=True)
    pe_blood_pressure = models.CharField("Presion Arterial", max_length=20,default='', blank=True)
    pe_temperature = models.CharField("Temperature", max_length=20,default='', blank=True)
    pe_oxygen_saturation = models.CharField("Saturacion O2", max_length=20,default='', blank=True)
    pe_glucometry = models.CharField("Glucometria", max_length=20,default='', blank=True)
    pe_glassgow = models.CharField("Glassgow", max_length=20,default='', blank=True)
    # Normal
    normal_head = models.CharField("Cabeza", blank=True, default='', max_length=10, choices=YES_NO)
    normal_face = models.CharField("Face", blank=True, default='', max_length=10, choices=YES_NO)
    normal_torax = models.CharField("Tórax", blank=True, default='', max_length=10, choices=YES_NO)
    normal_abdomen = models.CharField("Abdomen", blank=True, default='', max_length=10, choices=YES_NO)
    normal_limbs = models.CharField("Extremidades", blank=True, default='', max_length=10, choices=YES_NO)
    normal_genitals = models.CharField("Genitales", blank=True, default='', max_length=10, choices=YES_NO)
    normal_spine = models.CharField("Columna Vertebral", blank=True, default='', max_length=10, choices=YES_NO)

    current_condition = models.TextField("Padecimiento Actual",blank=True)

    pupil_state = models.CharField("Estado de las Pupilas",max_length=20, default='', blank=True ,choices=PUPIL_STATE)

    pathological_history_daibetes_melitus = models.CharField("Diabetes Melitus",blank= True, default=False, max_length=10, choices=YES_NO )
    pathological_history_arterial_hypertension = models.CharField("Hipertension Arterial",blank= True, default=False , max_length=10, choices=YES_NO)
    pathological_history_heart_disease = models.CharField("Cardiopatias",blank= True, default=False,max_length=10, choices=YES_NO)
    pathological_history_pneumopathies = models.CharField("Neumopatias",blank= True, default=False,max_length=10 , choices=YES_NO)
    pathological_history_trauma = models.CharField("Quirurgicos/Trauma",blank= True, default=False,max_length=10, choices=YES_NO)
    pathological_history_alergy = models.CharField("Alergias",blank= True, default=False, max_length=10, choices=YES_NO)

    current_therapeutics = models.TextField("Tiempo de Evolucion y Terapeutica Actual",blank=True)
    description_of_injuries = models.TextField("Descripcion de lesiones",blank=True)
    diagnostic_impresion = models.TextField("Impresion Diagnostica", blank=True)
    treatment = models.TextField("Tratamiento",blank=True)
    derivation = models.CharField("Derivacion",blank= True, default=False, max_length=20, choices=YES_NO)
    derivation_place = models.TextField("Notas Derivacion",blank= True )
    state_of_health = models.CharField("Derivacion",blank= True, default=False, max_length=20, choices=HEALTH_STATE)


    user = models.ForeignKey(User,verbose_name= "usuario",on_delete=models.DO_NOTHING, blank=True)
    # blood_products_solution 
    # Datetie utils
    created_at = models.DateTimeField("Fecha de alta",auto_now_add=True,editable=False)
    last_modified = models.DateTimeField("Última modificación",auto_now=True,editable=False)

    class Meta:
        verbose_name_plural = "Parte Medico"
        ordering = ['created_at']

    # Returns a verbose name - adjusted for Python3
    def __str__(self):
        return "{}, {}, {}, {}".format(unicodedata.normalize('NFKD',str(self.id)),unicodedata.normalize('NFKD', self.odoo_client), unicodedata.normalize('NFKD', self.patient_name), self.created_at)

