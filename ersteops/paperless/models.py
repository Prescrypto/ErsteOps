from django.db import models
#from unit.models import Unit
from django.contrib.auth.models import User
import unicodedata
import json
from django.core.validators import FileExtensionValidator
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
    INMOVILIZATION = (
        ('Columna Cervical','Columna Cervical'),
        ('Columna Toracica','Columna Toracica'),
        ('Extremidades','Extremidades'),
        ('Total','Total'),
        ('Otro','Otro'),
        )
    odoo_client = models.CharField("Cliente id(Legacy)", max_length=50,default ='',)
    erste_code = models.CharField("ID Code", max_length=50, blank=True, default="")
    odoo_client_name = models.CharField("Socio", max_length=200,blank=True, default="")
    service_code = models.CharField("Codigo de Servicio",max_length=10,default='')
    service_unit = models.CharField("Unidad Movil",max_length=10,default='')
    service_unit_type = models.CharField("Tipo Unidad",max_length=50,default='')
    service_unit_plate = models.CharField("No.Placas",max_length=10,default='')
    service_crum = models.CharField("Folio CRUM",max_length=20,default='', blank=True)
    service_crum_dr = models.CharField("Medico CRUM",max_length=60,default='', blank=True)
    # Units m2m relation
    # Paient Data
    copago_amount = models.CharField('Co-pago',max_length=10, blank=True ,default='')
    service_geo_lat = models.CharField('Latitud',max_length=25, blank=True ,default='')
    service_geo_lon = models.CharField('Longitud', max_length=25,  blank=True, default='')
    patient_name = models.CharField('Nombre del Paciente', max_length=255, default='')
    patient_gender = models.CharField('genero', max_length=15, default= '', blank=True, choices=GENDER)
    patient_age = models.IntegerField('edad (años)', default=0, blank=True)
    patient_address = models.CharField('Direccion', max_length=150, default='', blank=False)
    patient_affiliations = models.CharField("Filiacion",max_length=150,blank=True)
    is_patient_unknow = models.CharField("Es paciente desconocido",max_length=50,blank=True,default='')
    patient_unknow = models.CharField("Paciente Desconocido",max_length=50,blank=True)
    patient_clothes = models.CharField("Vestimenta", max_length=50,blank=True)
    patient_phone = models.CharField("Telefono:", max_length=50,blank=True ,default='')
    attention_place = models.CharField('Sitio de Atencion', max_length=20, default= '', blank=True, choices=ATENTION_PLACE)
    other_attention_place = models.CharField('Otro Sitio de Atencion', max_length=20, default= '', blank=True, choices=ATENTION_PLACE)
    skin_color = models.CharField("Coloración de piel", max_length=150, default= '', blank=True,)
    service_type = models.CharField('Tipo de Servicio', max_length=50, default= '', blank=True, choices=SERVICE_TYPE)
    other_service_type = models.CharField('Tipo de Servicio', max_length=50, default= '', blank=True)
    consultation_reason = models.CharField('Motivo de la Consulta', max_length=150, default= '', blank=True, choices=CONSULTATION_REASON)
    other_consultation_reason = models.CharField('Otro Motivo de la Consulta', max_length=50, default= '', blank=True)
    event_type = models.CharField('Tipo de Evento', max_length=20, default= '', blank=True, choices=EVENT_TYPE)
    traumatics = models.CharField('Traumatico', max_length=150, default= '', blank=True, choices=TRAUMATICS)
    other_traumatics = models.CharField('Otro Traumatico', max_length=150, default= '', blank=True, choices=TRAUMATICS)
    airway = models.TextField('Via Aerea', default= '', blank=True )
    other_airway = models.CharField('Otra Via Aerea', max_length=20, default= '', blank=True, choices=AIRWAY)
    
    physical_exploration = models.TextField("Exploracion Fisica",blank=True, default='')
    medications = models.TextField("Medicamentos",blank=True, default='')
    # Normal
    # (physical_exploration = pe)
    normal_head = models.CharField("Cabeza", blank=True, default='', max_length=10, choices=YES_NO)
    normal_face = models.CharField("Face", blank=True, default='', max_length=10, choices=YES_NO)
    normal_neck = models.CharField("Cuello", blank=True, default='', max_length=10, choices=YES_NO)
    normal_torax = models.CharField("Tórax", blank=True, default='', max_length=10, choices=YES_NO)
    normal_abdomen = models.CharField("Abdomen", blank=True, default='', max_length=10, choices=YES_NO)
    normal_limbs = models.CharField("Extremidades", blank=True, default='', max_length=10, choices=YES_NO)
    normal_genitals = models.CharField("Genitales", blank=True, default='', max_length=10, choices=YES_NO)
    normal_spine = models.CharField("Columna Vertebral", blank=True, default='', max_length=10, choices=YES_NO)

    det_normal_head = models.TextField("Notas Cabeza", blank=True)
    det_normal_face = models.TextField("Notas Cara", blank=True)
    det_normal_neck = models.TextField("Notas Cuello", blank=True)    
    det_normal_torax = models.TextField("Notas Tórax", blank=True)
    det_normal_abdomen = models.TextField("Notas Abdomen", blank=True)
    det_normal_limbs = models.TextField("Notas Extremidades", blank=True)
    det_normal_genitals = models.TextField("Notas Genitales", blank=True)
    det_normal_spine = models.TextField("Notas Columna Vertebral", blank=True)


    current_condition = models.TextField("Padecimiento Actual",blank=True)

    pupil_state_left = models.CharField("Estado de la pupila, Izquierda",max_length=150, default='', blank=True ,choices=PUPIL_STATE)
    pupil_state_right = models.CharField("Estado de la pupilas, Derecha",max_length=150, default='', blank=True ,choices=PUPIL_STATE)
    inmovilization = models.CharField("Inmovilizacion",max_length=150, default='', blank=True)
    inmovilization_type = models.CharField("Inmovilizacion",max_length=150, default='', blank=True, choices=INMOVILIZATION)
    other_inmovilization_type = models.CharField("Otra Inmovilizacion",max_length=150, default='', blank=True)

    pathological_history_daibetes_melitus = models.CharField("Diabetes Melitus",blank= True, default=False, max_length=10, choices=YES_NO )
    pathological_history_arterial_hypertension = models.CharField("Hipertension Arterial",blank= True, default=False , max_length=10, choices=YES_NO)
    pathological_history_heart_disease = models.CharField("Cardiopatias",blank= True, default=False,max_length=10, choices=YES_NO)
    pathological_history_pneumopathies = models.CharField("Neumopatias",blank= True, default=False,max_length=10 , choices=YES_NO)
    pathological_history_trauma = models.CharField("Quirurgicos/Trauma",blank= True, default=False,max_length=10, choices=YES_NO)
    pathological_history_alergy = models.CharField("Alergias",blank= True, default=False, max_length=10, choices=YES_NO)
    other_pathological_history = models.CharField("Otra enfermedad",blank= True, default=False, max_length=250)

    detail_pat_history_daibetes_melitus = models.TextField("Notas Diabetes Melitus",blank= True )
    detail_pat_history_arterial_hypertension = models.TextField("Notas Hipertension Arterial",blank= True)
    detail_pat_history_heart_disease = models.TextField("Notas Cardiopatias",blank= True)
    detail_pat_history_pneumopathies = models.TextField("Notas Neumopatias",blank= True)
    detail_pat_history_trauma = models.TextField("Notas Quirurgicos/Trauma",blank= True)
    detail_pat_history_alergy = models.TextField("Notas Alergias",blank= True )

    current_therapeutics = models.TextField("Tiempo de Evolucion y Terapeutica Actual",blank=True)
    description_of_injuries = models.TextField("Descripcion de lesiones",blank=True)
    diagnostic_impresion = models.TextField("Impresion Diagnostica", blank=True)
    treatment = models.TextField("Tratamiento",blank=True)
    derivation = models.CharField("Derivacion",blank= True, default=False, max_length=20, choices=YES_NO)
    derivation_type = models.CharField("Tipo Derivacion",blank= True, default=False, max_length=20, choices=DERIVATION)
    derivation_amount= models.CharField('Costo Derivacion', max_length=20,default='', blank=True)
    derivation_place = models.TextField("Notas Derivacion",blank= True )
    state_of_health = models.CharField("Estado de Salud",blank= True, default=False, max_length=20, choices=HEALTH_STATE)
    derivation_recive = models.CharField("Medico que recibe",blank= True, default=False, max_length=50)
    demarcation = models.CharField("Deslinde",blank= True, default=False, max_length=20, choices=YES_NO)
    demarcation_responsable = models.CharField("Deslinde responsable",blank= True, default=False, max_length=50)
    demarcation_relation = models.CharField("Deslinde relacion",blank= True, default=False, max_length=20)
    crum = models.CharField("Folio CRUM",blank= True, default=False, max_length=20)
    crum_reception = models.CharField("Medico Recibe CRUM",blank= True, default=False, max_length=120)    

    user = models.ForeignKey(User,verbose_name= "usuario",on_delete=models.DO_NOTHING, blank=True)
    # blood_products_solution 
    # Datetie utils
    created_at = models.DateTimeField("Fecha de alta",auto_now_add=True,editable=False)
    last_modified = models.DateTimeField("Última modificación",auto_now=True,editable=False)

    electro_rhythm = models.CharField("Ritmo", blank=True, default='', max_length=50)
    electro_frequency = models.CharField("Frecuencia", blank=True, default='', max_length=50)
    electro_wave_p = models.CharField("Onda P", blank=True, default='', max_length=50)
    electro_pr = models.CharField("PR", blank=True, default='', max_length=50)
    electro_axis_qrs = models.CharField("Eje QRS", blank=True, default='', max_length=50)
    electro_st = models.CharField("ST", blank=True, default='', max_length=50)
    electro_wave_t = models.CharField("Onda T", blank=True, default='', max_length=50)
    electro_qt = models.CharField("QT", blank=True, default='', max_length=50)
    electro_abnormalities = models.TextField("Anormalidades", blank=True, default='', max_length=100)
    electro_interpretation = models.TextField("Interpretacion", blank=True, default='') 

    electro_qrs = models.CharField("QRS", blank=True, default='', max_length=20)
    email = models.CharField("Email", blank=True, default='', max_length=50)
    send_email = models.CharField("Se envio Email", blank=True, default='', max_length=20)
    derivation_hospital = models.CharField("Hospitar derivacion", blank=True, default='', max_length=100)
    crum_hospital = models.CharField("Hospitar recibe CRUM", blank=True, default='', max_length=100)
    crum_notes = models.TextField("Notas Crum",blank=True)
    notes = models.TextField("Notas Emergencia",blank=True)
    crew_medic = models.CharField("Medico CREW",blank=True,default='',max_length=50)
    crew_medic_id_card = models.CharField("Cedula Profesional",blank=True,default='',max_length=50)
    crew_tum = models.CharField("TUM",blank=True,default='',max_length=50)
    crew_operator = models.CharField("Operador",blank=True,default='',max_length=50) 
    final_report = models.FileField("archivo de estudios(pdf o jpg)",validators=[FileExtensionValidator(allowed_extensions=['pdf','jpg'])],max_length=100,upload_to="pdffile/pdf_files",default="",blank=True)
    signature_client = models.TextField('Signature Client',blank=True)
    signature_medic = models.TextField('Signature Medic',blank=True)

    def json_physical_exploration(self):
        #convert_to_json
        try:
            res = list(eval(self.physical_exploration))
        except:
            res = []
        return res

    def json_medications(self):
        #convert_to_json
        try:
            res = list(eval(self.medications))
        except:
            res = []
        return res
    def json_airway(self):
        #convert_to_json
        try:
            res = list(eval(self.airway))
        except:
            res = []
        return res 

    def json_consultation_reason(self):
        #convert_to_json
        try:
            res = list(eval(self.consultation_reason))
        except:
            res = []
        return res        

    def json_pupil_state_left(self):
        #convert_to_json
        try:
            res = list(eval(self.pupil_state_left))
        except:
            res = []
        return res   

    def json_pupil_state_right(self):
        #convert_to_json
        try:
            res = list(eval(self.pupil_state_right))
        except:
            res = []
        return res   

    def json_traumatics(self):
        #convert_to_json
        try:
            res = list(eval(self.traumatics))
        except:
            res = []
        return res
    
    def json_inmovilization_type(self):
        #convert_to_json
        try:
            res = list(eval(self.inmovilization_type))
        except:
            res = []
        return res



    class Meta:
        verbose_name_plural = "Parte Medico"
        ordering = ['created_at']

    # Returns a verbose name - adjusted for Python3
    def __str__(self):
        return "{}, {}, {}, {}".format(unicodedata.normalize('NFKD',str(self.id)),unicodedata.normalize('NFKD', self.odoo_client), unicodedata.normalize('NFKD', self.patient_name), self.created_at)



