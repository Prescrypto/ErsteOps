from django.conf.urls import url

from .views import unit_json_list, alliance_unit_json_list, detail_unit_json

urlpatterns = [
    # Ajax Views
    url(r'^ajax/detail/(?P<id_unit>[0-9]+)$', detail_unit_json, name="detail_unit_json"),
    url(r'^ajax/local/$', unit_json_list, name="local_units_json_list"),
    url(r'^ajax/alliance/$', alliance_unit_json_list, name="alliance_units_json_list"),
]
