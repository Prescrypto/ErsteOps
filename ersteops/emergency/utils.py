import logging
import json
from django.utils import timezone
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from .models import Emergency
from .forms import EmergencyForm
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

class UpdateJsonResponseMixin(object):
    '''' Mixin to add on update emergency view '''
    logger = logging.getLogger('django_info')

    def form_invalid(self, form):
        response = super(UpdateJsonResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            data = json.loads(self.request.body.decode('utf-8'))
            if data:
                self.logger.info("POST Data: {}".format(data))
                emergency_object = super(UpdateJsonResponseMixin, self).get_object()
                emergency_form = EmergencyForm(data, instance=emergency_object)
                # add new field
                # emergency_form.data.update({'start_time': timezone.now()})
                if emergency_form.is_valid():
                    self.object = emergency_form.save()
                    data_object = {
                        'id': self.object.pk,
                    }
                    self.logger.info("POST new Emergency] AJAX FORM SUCCESS")
                    return JsonResponse(data_object, status=200)
                else:
                    self.logger.info("[POST new Emergency] AJAX FORM ERRORS:{}".format(emergency_form.errors))
                    return JsonResponse(emergency_form.errors, status=400)

        self.logger.info("[POST new Emergency] form: Error AJAX")
        return JsonResponse(form.errors, status=400)



class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    logger = logging.getLogger('django_info')

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            data = json.loads(self.request.body.decode('utf-8'))
            if data:
                self.logger.info("Data: {}".format(data))
                emergency_form = EmergencyForm(data)
                emergency_form.data.update({'start_time': timezone.now()})
                if emergency_form.is_valid():
                    self.object = emergency_form.save()
                    data_object = {
                        'id': self.object.pk,
                    }
                    self.logger.info("POST new Emergency] AJAX FORM SUCCESS")
                    return JsonResponse(data_object, status=200)
                else:
                    self.logger.info("[POST new Emergency] AJAX FORM ERRORS:{}".format(emergency_form.errors))
                    return JsonResponse(emergency_form.errors, status=400)

            self.logger.info("[POST new Emergency] form: Error AJAX")
            return JsonResponse(form.errors, status=400)
        else:
            self.logger.info("[POST new Emergency] form: Error Normal")
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            self.logger.info("[POST new Emergency] form: Success AJAX")
            self.object = form.save()
            data = {
                'id': self.object.pk,
            }
            return JsonResponse(data, status=200)
        else:
            self.logger.info("[POST new Emergency] form: Success Normal")
            return response
