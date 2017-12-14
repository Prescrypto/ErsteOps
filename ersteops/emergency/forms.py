# -*- encoding: utf-8 -*-
# From Forms
from django import forms
from django.forms.models import inlineformset_factory
from django.forms import extras
from django.forms import formset_factory

class OdooClientForm(forms.Form):
    CHOICES = (
        ("1","Nobre del paciente"),
        ("2","Direccion"),
        ("3","id cliente"),
        ("4","get token"),
        ("5","get all patients"),
        )

    client_name = forms.CharField(
    label='Cliente Odoo',
    required=True,
    #help_text='Ingresa el nombre del cliente',
    widget=forms.TextInput(attrs={
      'class': 'form-control ui-widget',
      'placeholder': 'Indica la cadena a buscar',
      'title': 'Titulo',
      'max_length': '20',
    }))

    search_type = forms.ChoiceField(
    label = 'Buscar por:',
    required = False,
    widget = forms.Select(attrs={'class': 'form-control ui-widget edit_selector',}),
    choices = CHOICES
  )

class OdooClientAuto(forms.Form):
  client_id = forms.CharField(
    label = 'client_id',
    required = False,
    initial = 0,
    widget = forms.HiddenInput(attrs={'is_hidden': 'True'})
    )
  client_name = forms.CharField(
    label='Nombre del cliente en Odoo',
    required=True,
    #help_text='Ingresa el nombre del cliente',
    widget=forms.TextInput(attrs={
      'class': 'form-control ui-widget',
      'placeholder': 'Indica la cadena a buscar',
      'title': 'Titulo',
      'max_length': '20',
    }))

