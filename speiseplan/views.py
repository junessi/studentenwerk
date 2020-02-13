import json
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

base_url = "http://127.0.0.1/redirect/studentenwerk_openmensa_api/openmensa/v2"

def list_canteens(request):
    url = base_url + "/canteens"

    return HttpResponse(requests.get(url))

def canteen_info(request, canteen_id):
    url = base_url + "/canteens/" + canteen_id

    return HttpResponse(requests.get(url))

def canteen_dates(request, canteen_id, date):
    url = base_url + "/canteens/" + canteen_id + "/days/" + date

    return HttpResponse(requests.get(url))

def canteen_meals(request, canteen_id, date):
    url = base_url + "/canteens/" + canteen_id + "/days/" + date + "/meals/"

    return HttpResponse(requests.get(url))

def canteen_meal_detail(request, canteen_id, date, meal_id):
    url = base_url + "/canteens/" + canteen_id + "/days/" + date + "/meals/" + meal_id

    return HttpResponse(requests.get(url))

