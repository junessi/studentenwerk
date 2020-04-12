import json
import requests
import array
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from query.meal import MealQuery, Meal

base_url = "https://api.studentenwerk-dresden.de/openmensa/v2"

def list_canteens(request):
    url = base_url + "/canteens"

    return JsonResponse(requests.get(url).json(), safe = False)

def canteen_info(request, canteen_id):
    url = base_url + "/canteens/" + canteen_id

    return JsonResponse(requests.get(url).json(), safe = False)

def canteen_dates(request, canteen_id):
    url = base_url + "/canteens/" + canteen_id + "/days/"

    days = requests.get(url).json()
    for day in days:
        day["closed"] = False
    return JsonResponse(days, safe = False)
    # return JsonResponse(requests.get(url).json(), safe = False)

def canteen_date(request, canteen_id, date):
    url = base_url + "/canteens/" + canteen_id + "/days/" + date

    return JsonResponse(requests.get(url).json(), safe = False)

def canteen_meals(request, canteen_id, date):
    url = base_url + "/canteens/" + canteen_id + "/days/" + date + "/meals/"

    # meals = requests.get(url).json()
    meals = [{ "id": 260,
                    "name": "Gemüse-Couscouspfanne mit Joghurt-Ingwer-Dip, dazu bunter Blattsalat",
                    "notes": ["ovo-lacto-vegetabil", "mensaVital"],
                    "prices": {"students": 2.3, "employees": 3.65, "others": 4.6},
                    "category": "Alternativ-Angebot",
                    "likes": 0
                 },
                 {
                    "id": 10900,
                    "name": "Hähnchenschnitzel mit Brötchen",
                    "notes": [],
                    "prices": { "pupils": 2.4, "others": 4.3},
                    "category": "Cafeteria Heiße Theke",
                    "likes": 0
                 }]

    # extend meal info
    for m in meals:
        result = MealQuery().get_meal(m["id"])
        if len(result):
            likes_count = len(array.array('L', result[0].liked_users).tolist())
            m["likes"] = likes_count
        else:
            meal = Meal(m["id"])
            meal.save()

    return JsonResponse(meals, safe = False)
    # return JsonResponse(meals, safe = False)

def canteen_meal_detail(request, canteen_id, date, meal_id):
    url = base_url + "/canteens/" + canteen_id + "/days/" + date + "/meals/" + meal_id

    return JsonResponse(requests.get(url).json(), safe = False)

def likes(request, canteen_id, date, meal_id):
    
    wechat_uid = 0
    liked_users = []
    updated = False
    result = MealQuery().get_meal(meal_id)

    if len(result):
        liked_users = array.array('L', result[0].liked_users).tolist()

        if "action" in request.GET and "wechat_uid" in request.GET:
            if request.GET["action"] == "like":
                if int(request.GET["wechat_uid"]) not in liked_users:
                    liked_users.append(int(request.GET["wechat_uid"]))

                    updated = True
            elif request.GET["action"] == "unlike":
                if int(request.GET["wechat_uid"]) in liked_users:
                    liked_users.remove(int(request.GET["wechat_uid"]))

                    updated = True

            if updated:
                result[0].liked_users = array.array('L', liked_users)
                result[0].update_data()

    return JsonResponse({"status": 200, "liked_users": liked_users}, safe = False)

