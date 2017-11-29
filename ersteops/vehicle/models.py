from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from datetime import datetime

# Create your models here.
@python_2_unicode_compatible
class Unit(models.Model):
    MODEL_YEAR = (
        ("2006","2006"),
        ("2007","2007"),
        ("2008","2008"),
        ("2009","2009"),
        ("2010","2010"),
        ("2011","2011"),
        ("2012","2012"),
        ("2013","2013"),
        ("2014","2014"),
        ("2015","2015"),
        ("2016","2016"),
        ("2017","2017"),
        ("2018","2018"),
        ("2019","2019"),
        ("2020","2020"),
        ("2021","2021"),
        ("2022","2022"),
        ("2023","2023"),
        ("2024","2024"),
        ("2025","2025"),
        ("2026","2026"),
    )
    unit_id = models.IntegerField("id",primary_key=True,unique=True)
    model = models.CharField("modelo",max_length=50,default="")
    year = models.CharField("año de fabricacion",max_length=4,default= 0,choices = MODEL_YEAR)
    license_plate = models.CharField("placa",max_length=10,unique=True)
    brand = models.ForeignKey("Brand",
    related_name="brand_name",
    verbose_name= "marca"
        )
    unit_type = models.ForeignKey("UnitType",
    related_name="unit_type_name",
    verbose_name= "tipo de unidad"
        )
    is_active = models.NullBooleanField("activa")
    assigned = models.NullBooleanField("asignada")
    created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
    last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
    class Meta:
        verbose_name_plural = "Unidad"
        ordering = ['created_at']
    def __str__(self):  
        return str(self.unit_id) + ' - '+ self.unit_type.name

@python_2_unicode_compatible
class Brand(models.Model):
    name = models.CharField("marca",max_length=50,unique=True)
    created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
    last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
    class Meta:
        verbose_name_plural = "Marca"
        ordering = ['name']
    def __str__(self):  
        return self.name

@python_2_unicode_compatible
class UnitType(models.Model):
    name = models.CharField("tipo",max_length=50,unique=True)
    created_at = models.DateTimeField("fecha de alta",auto_now_add=True,editable=False)
    last_modified = models.DateTimeField("ultima modificacion",auto_now=True,editable=False)
    class Meta:
        verbose_name_plural = "Tipo de Unidad"
        ordering = ['name']
    def __str__(self):  
        return self.name
