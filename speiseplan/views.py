import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from caterings.wueins import WUEins


@csrf_exempt
def speise_plan(request, catering_name):
    """
    List all code meals
    """
    if request.method == 'GET':
        we = WUEins()

        return JsonResponse(we.serialized_data(), safe=False)

