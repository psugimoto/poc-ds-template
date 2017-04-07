# coding: utf-8
from __future__ import unicode_literals

import json

from django.views.generic import View
from django.conf import settings
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed

from . import models


def load(request, *args, **kwargs):
    if request.method.upper() != 'POST':
        return HttpResponseNotAllowed(['POST'])  # List of allowed ones

    if models.load_model():
        return JsonResponse({
            'message': 'Model loaded',
        })
    else:
        return JsonResponse({
            'message': 'Model does not exist',
        }, status=500)


class EvaluateView(View):
    def get(self, *args, **kwargs):
        valuation = models.evaluate()
        if valuation is None:
            return JsonResponse({
                'message': 'Model is not available',
            }, status=500)

        return JsonResponse({'precision': models.evaluate()})


class PredictView(View):
    def post(self, *args, **kwargs):
        if models.model is None:
            models.load_model()

        data = self.request.POST.dict()    # should not be needed!
        return JsonResponse({
            'predicted': models.predict(data),
        }, status=200)
