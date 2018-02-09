from django.conf.urls import url

from .views import unit_json_list, alliance_unit_json_list

urlpatterns = [
    # Ajax Views
    url(r'^ajax/local/$', unit_json_list, name="local_units_json_list"),
    url(r'^ajax/alliance/$', alliance_unit_json_list, name="alliance_units_json_list"),
]
