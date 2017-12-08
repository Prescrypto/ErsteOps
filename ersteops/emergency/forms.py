# -*- encoding: utf-8 -*-
# From Forms
from django import forms
from django.forms.models import inlineformset_factory
from django.forms import extras
from django.forms import formset_factory

class OdooClientForm(forms.Form):
    client_name = forms.CharField(
    label='Cliente Odoo',
    required=True,
    #help_text='Ingresa el nombre del cliente',
    widget=forms.TextInput(attrs={
      'class': 'form-control',
      'placeholder': 'Indica la cadena a buscar',
      'title': 'Titulo',
      'max_length': '20',

      })
    )


