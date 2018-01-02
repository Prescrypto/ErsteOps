from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from .models import Emergency

class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return HttpResponse(
            self.get_data(context),
            content_type='application/json',
            **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        fields = (
            'id',
            'odoo_client',
            'service_category',
            'grade_type',
            'zone',
            'start_time',
            'end_time',
            'is_active',
            'unit',
            'unit_assigned_time',
            'unit_dispatched_time',
            'arrival_time',
            'attention_time',
            'derivation_time',
            'hospital_arrival',
            'patient_arrival',
            'final_emergency_time',
            'address_street',
            'address_extra',
            'address_zip_code',
            'address_county',
            'address_col',
            'address_between',
            'address_and_street',
            'address_ref',
            'address_front',
            'address_instructions',
            'address_notes',
            'caller_name',
            'caller_relation',
            'patient_name',
            'patient_gender',
            'patient_age',
            'patient_allergies',
            'patient_illnesses',
            'patient_notes',
            'attention_final_grade',
            'attention_justification',
            'main_complaint',
            'complaint_descriprion',
            'subscription_type',
        )
        emergency = Emergency.objects.filter(id=context["object"].id)
        data = serializers.serialize('json', emergency, fields=fields)
        return data