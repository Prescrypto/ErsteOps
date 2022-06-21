from django import forms
from .models import MedicalReport

class MedicalReportForm(forms.Form):
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
  error_css_class = 'error'
  required_css_class = 'required'
  service_geo_lat = forms.CharField(
    label = 'service_geo_lat',
    required = False,
    initial = "",
    widget = forms.HiddenInput(attrs={'is_hidden': 'True'})
    )
  service_geo_lon = forms.CharField(
    label = 'service_geo_lon',
    required = False,
    initial = "",
    widget = forms.HiddenInput(attrs={'is_hidden': 'True'})
    )
  service_code = forms.CharField(
    label = '* Codigo de Servicio:',
    required = True,
    widget = forms.TextInput(attrs = {
      'class': 'form-control ui-widget patient uk-input uk-form-label',
      'placeholder': 'Codigo de servicio',
      'max_length': '100'
      })
    )
  service_unit = forms.CharField(
    label = '* Unidad Movil:',
    required = True,
    widget = forms.TextInput(attrs = {
      'class': 'form-control ui-widget patient uk-input uk-form-label',
      'placeholder': 'M011',
      'max_length': '100'
      })
    )
  service_unit_type = forms.CharField(
    label = '* Tipo Unidad:',
    required = True,
    widget = forms.TextInput(attrs = {
      'class': 'form-control ui-widget patient uk-input uk-form-label',
      'placeholder': 'Tipo Unidad',
      'max_length': '100'
      })
    )
  service_unit_plate = forms.CharField(
    label = '* No.Placas:',
    required = True,
    widget = forms.TextInput(attrs = {
      'class': 'form-control ui-widget patient uk-input uk-form-label',
      'placeholder': 'Placa',
      'max_length': '100'
      })
    )      
  patient_name = forms.CharField(
    label = '* Nombre del Paciente:',
    required = True,
    widget = forms.TextInput(attrs = {
      'class': 'form-control ui-widget patient uk-input uk-form-label',
      'placeholder': 'Nombre del paciente',
      'max_length': '100'
      })
    )

  patient_gender = forms.ChoiceField(
    label = '* Genero',
    required = True,
    widget = forms.Select(attrs={'class': 'form-control ui-widget ed_sel_patient patient uk-input uk-form-label',}),
    choices = GENDER
    )
  patient_age = forms.IntegerField(
    label = '* Edad',
    required = True, 
    widget = forms.NumberInput( attrs = {
      'class': 'form-control ui-widget uk-input uk-form-label',
      })
    )
  patient_affiliations = forms.CharField(
    label = 'Filiacion:',
    required = False,
    widget = forms.TextInput(attrs = {
      'class': 'form-control ui-widget patient uk-input uk-form-label',
      'placeholder': 'Filiacion del paciente',
      'max_length': '100'
      })
    )
  patient_unknow = forms.CharField(
    label = 'Paciente desconocido:',
    required = False,
    widget = forms.TextInput(attrs = {
      'class': 'form-control ui-widget patient uk-input uk-form-label',
      'placeholder': 'Paciente Desconocido',
      'max_length': '100'
      })
    )
  patient_clothes = forms.CharField(
    label = 'Vestimenta:',
    required = False,
    widget = forms.TextInput(attrs = {
      'class': 'form-control ui-widget patient uk-input uk-form-label',
      'placeholder': 'Vestimenta',
      'max_length': '100'
      })
    )
  skin_color = forms.CharField(
    label = 'Coloracion de piel:',
    required = False,
    widget = forms.TextInput(attrs = {
      'class': 'form-control ui-widget patient uk-input uk-form-label',
      'placeholder': 'Coloracion de piel',
      'max_length': '100'
      })
    )
  attention_place = forms.ChoiceField(
    label = 'Sitio de Atencion',
    required = True,
    widget = forms.Select(attrs={'class': 'form-control ui-widget ed_sel_patient patient uk-input uk-form-label',}),
    choices = ATENTION_PLACE
    )
  service_type = forms.ChoiceField(
    label = 'Tipo de Servicio',
    required = True,
    widget = forms.Select(attrs={'class': 'form-control ui-widget ed_sel_patient patient uk-input uk-form-label',}),
    choices = SERVICE_TYPE
    )
  consultation_reason = forms.ChoiceField(
    label = 'Motivo de la consulta',
    required = False,
    widget = forms.Select(attrs={'class': 'form-control ui-widget ed_sel_patient patient uk-input uk-form-label',}),
    choices = CONSULTATION_REASON
    )
  traumatics = forms.ChoiceField(
    label = 'Traumaticos',
    required = False,
    widget = forms.Select(attrs={'class': 'form-control ui-widget ed_sel_patient patient uk-input uk-form-label',}),
    choices = TRAUMATICS
    )
  airway = forms.ChoiceField(
    label = 'Via Aerea',
    required = False,
    widget = forms.Select(attrs={'class': 'form-control ui-widget ed_sel_patient patient uk-input uk-form-label',}),
    choices = AIRWAY
    )
  pupil_state = forms.ChoiceField(
    label = 'Estado de las Pupilas',
    required = False,
    widget = forms.Select(attrs={'class': 'form-control ui-widget ed_sel_patient patient uk-input uk-form-label',}),
    choices = PUPIL_STATE
    )
  current_condition = forms.CharField(
    label = 'Padecimiento Actual:',
    required = False,
    widget = forms.TextInput(attrs = {
      'class': 'form-control ui-widget patient uk-input uk-form-label',
      'placeholder': 'Padecimiento actual',
      'max_length': '100'
      })
    )
  pathological_history_daibetes_melitus = forms.ChoiceField(
    label = 'Antecedentes Patologicos - Diabetes:',
    required = False,
    widget = forms.Select(attrs={'class': 'form-control ui-widget ed_sel_patient patient uk-input uk-form-label',}),
    choices = YES_NO
    )
  pathological_history_arterial_hypertension = forms.ChoiceField(
    label = 'Antecedentes Patologicos - Hipertension Arterial:',
    required = False,
    widget = forms.Select(attrs={'class': 'form-control ui-widget ed_sel_patient patient uk-input uk-form-label',}),
    choices = YES_NO
    )
  