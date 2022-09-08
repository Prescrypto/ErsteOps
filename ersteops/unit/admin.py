from django.contrib import admin
from .models import Unit, CrewRoll, CrewMember, TodayUnitDoctor

class UnitAdmin(admin.ModelAdmin):
    ''' Customize Unit Admin '''
    list_display = ("identifier", "unit_type", "is_active", "is_assigned", "is_alliance", "location", "operator", "phone")
    list_filter = ("unit_type", "is_active", "is_assigned", "is_alliance", )
    search_fields = ('identifier', 'location', 'phone', )

admin.site.register(Unit, UnitAdmin)
admin.site.register(CrewRoll)
admin.site.register(CrewMember)
admin.site.register(TodayUnitDoctor)
