from django.core import serializers
from django.http import HttpResponse
from .models import Unit
from .utils import UNIT_LIST_FIELD

def unit_json_list(request):
    ''' List Json View for local available units '''
    units = Unit.objects.available_units()
    data = serializers.serialize('json', list(units), fields=UNIT_LIST_FIELD)
    return HttpResponse(data, content_type='application/json')

def alliance_unit_json_list(request):
    ''' List Json View for alliance available units '''
    units = Unit.objects.available_alliance_units()
    data = serializers.serialize('json', list(units), fields=UNIT_LIST_FIELD)
    return HttpResponse(data, content_type='application/json')
