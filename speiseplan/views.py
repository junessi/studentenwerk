import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from caterings.wueins import WUEins
from speiseplan.models import Catering, MealDate, Meal
from speiseplan.serializer import CateringSerializer, MealDateSerializer, MealSerializer


@csrf_exempt
def speise_plan(request, catering_name):
    """
    List all code meals
    """
    if request.method == 'GET':
        we = WUEins()

        """
        c = Catering(id=0, name="WUEins")
        c.save()
        serializer = CateringSerializer(instance=c)
        md0 = MealDate(catering=c, text="today")
        md0.save()
        md1 = MealDate(catering=c, text="tomorrow")
        md1.save()
        m0 = Meal(catering=c, mealdate=md0, name="DAN", price0="1", price1="2")
        m0.save()
        m1 = Meal(catering=c, mealdate=md0, name="FANQIE", price0="3", price1="4")
        m1.save()
        """

        # print(we.serialize())
        return JsonResponse(we.serialize(), safe=False)
        # return JsonResponse(serializer.data, safe=False)

