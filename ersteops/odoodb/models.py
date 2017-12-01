from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
import unicodedata
from datetime import datetime
from django.utils import timezone

# Create your models here.

@python_2_unicode_compatible
class res_partner(models.Model):
    id = models.IntegerField(default=0,primary_key=True)
    name = models.CharField(default=0,max_length=80)
    class Meta:
        verbose_name_plural = "Partner"
        ordering = ['id']
        managed = False
        #db_table = '"public"."res_partner"'
        db_table = "res_partner"
        #db_table = 'res_partner'
    def __str__(self):
        return self.name
