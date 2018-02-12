# coding=utf-8

from django.db import models

from .utils import UNIT_TYPE_LIST

class UnitQueryset(models.QuerySet):
    ''' Add custom querysets'''

    def available_units(self):
        return self.filter(is_active=True).filter(is_assigned=False).filter(is_alliance=False)

    def available_alliance_units(self):
        return self.filter(is_active=True).filter(is_alliance=True)


class UnitManager(models.Manager):
    ''' Manager for prescriptions '''

    def get_queryset(self):
        return UnitQueryset(self.model, using=self._db)

    def available_units(self):
        return self.get_queryset().available_units()

    def available_alliance_units(self):
        return self.get_queryset().available_alliance_units()


# I.e. Return all units available
# Unit.objects.available_units()
# Return all alliance units available
# Unit.objects.available_alliance_units()

class Unit(models.Model):
    ''' Unit model for ErsteOps '''

    # List of Unit type choices
    UNIT_TYPE_CHOICES = UNIT_TYPE_LIST

    # Required fields
    identifier = models.CharField('Identificador', unique=True, max_length=255, default='', help_text='ID de Unidad o Nombre de Alianza')
    unit_type = models.CharField('Tipo de unidad', max_length=255, choices=UNIT_TYPE_CHOICES)

    # Logical fields
    is_active = models.BooleanField('Esta activa', default=True, help_text='Define si es una unidad activa')
    is_assigned = models.BooleanField('Esta asignada', default=False, help_text='Define si la unidad esta asignada o disponible')
    is_alliance = models.BooleanField('Es alianza', default=False, help_text='Define si es unidad de alianza')

    # Primary Optional fields
    location = models.CharField('Base/Zona', max_length=300, blank=True, default='', help_text='Base para Locales y Zona para Alianzas')
    operator = models.CharField('Operador', max_length=50, blank=True, default='', help_text='Nombre del Operador de la unidad')
    phone = models.CharField('Teléfono', max_length=50, blank=True, default='', help_text='Sólo necesario si es alianza')

    # Secundary optional fields
    description = models.TextField('Descripción de la unidad', blank=True, default="", help_text='Datos como modelo, placa, mantenimiento, etc.')

    # Helpers time fields
    created_at = models.DateTimeField("Fecha de alta", auto_now_add=True)
    last_modified = models.DateTimeField("Última modificación", auto_now=True)

    objects = UnitManager()

    class Meta:
        verbose_name_plural = "Unidades"

    def __str__(self):
        ''' Return identifier as name '''
        return self.identifier
