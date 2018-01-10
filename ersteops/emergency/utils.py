from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from .models import Emergency
from .list_fields import EMERGENCY_LIST_FIELDS

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
        fields = EMERGENCY_LIST_FIELDS
        emergency = Emergency.objects.filter(id=context["object"].id)
        data = serializers.serialize('json', emergency, fields=fields)
        return data