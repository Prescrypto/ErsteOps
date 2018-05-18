# -*- coding: utf-8 -*-

from django.db import models
from django.forms.models import model_to_dict

from .utils import UNIT_TYPE_LIST

class UnitQueryset(models.QuerySet):
    ''' Add custom querysets'''

    def available_units(self):
        # add alliances removing alliance filter
        return self.filter(is_active=True).filter(is_assigned=False)

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


class CrewRoll(models.Model):
    ''' Crew type ej Medic, First Responder, Pilot '''
    name = models.CharField('Tipo de integrante',max_length=255, default='', unique=True)
    description = models.TextField('Descripción del Rol', blank=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Tipos de Tripulación"

    def __str__(self):
        ''' Return identifier as name '''
        return self.name


class CrewMember(models.Model):
    ''' Crew members, each unit can have one or many crew members '''
    name = models.CharField('Nombre del miembro tripulante', max_length=255, default='')
    crewroll = models.ForeignKey("CrewRoll",
        related_name="crew_members",
        verbose_name= "Tipo de tripulación"
        )
    more_info = models.TextField("Más Información acerca del miembro tripulante", blank=True)

    # Datetime utils
    created_at = models.DateTimeField("Fecha de alta", auto_now_add=True)
    last_modified = models.DateTimeField("Última modificación", auto_now=True)

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "Miembros de Tripulación"

    def __str__(self):
        ''' Return identifier as name '''
        return "{} - {}".format(self.crewroll.name, self.name)


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

    # Crew
    crew = models.ManyToManyField('CrewMember', related_name='units', verbose_name= "Miembros de Tripulación", blank=True)

    class Meta:
        verbose_name_plural = "Unidades"

    def __str__(self):
        ''' Return identifier as name '''
        return self.identifier

    @property
    def get_crew_list(self):
        ''' get list of crew '''
        if self.crew.all().count() > 0:
            member_list = []
            for member in self.crew.all():
                # Serialize crew members
                crew = model_to_dict(member)
                crew.update({'label': member.__str__()})
                member_list.append(crew)

            return member_list
        else:
            return []


