import json
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.http import HttpResponse
from .models import Unit
from .utils import UNIT_LIST_FIELD

BAD_REQUEST = HttpResponse(json.dumps({'error': 'Bad Request'}), status=400, content_type='application/json')

def unit_json_list(request):
    ''' List Json View for local available units '''
    if request.is_ajax():
        units = Unit.objects.available_units()
        data = serializers.serialize('json', list(units), fields=UNIT_LIST_FIELD)
        _raw_data = json.loads(data)
        for unit in _raw_data:
            if unit['fields']['is_alliance']:
                unit['fields'].update({'identifier': '{}{}'.format(unit['fields']['identifier'],' (Alianza)')})
            else:
                continue
        return HttpResponse(json.dumps(_raw_data), content_type='application/json', status=200)
    else:
        return BAD_REQUEST

def detail_unit_json(request, id_unit):
    ''' Detail view of unit '''
    if request.is_ajax():
        unit = Unit.objects.filter(pk=id_unit)

        if len(unit) == 0:
            return HttpResponse(json.dumps({'error': 'Unidad no encontrada'}), status=404, content_type='application/json')

        data = serializers.serialize('json', unit, fields=UNIT_LIST_FIELD)
        # Add crew list
        _raw_data = json.loads(data)
        _raw_data[0]['fields'].update({
            'crew_list' : unit.first().get_crew_list
        })
        return HttpResponse(json.dumps(_raw_data), content_type='application/json', status=200)
    else:
        return BAD_REQUEST

def alliance_unit_json_list(request):
    ''' List Json View for alliance available units '''
    if request.is_ajax():
        units = Unit.objects.available_alliance_units()
        data = serializers.serialize('json', list(units), fields=UNIT_LIST_FIELD)
        return HttpResponse(data, content_type='application/json', status=200)
    else:
        return BAD_REQUEST
