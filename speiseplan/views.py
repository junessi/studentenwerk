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
    # url = base_url + "/canteens/" + canteen_id + "/days/" + date + "/meals/"
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
            liked_users = array.array('L', result[0].liked_users).tolist()
            m["liked"] = False
            m["likes"] = len(liked_users)
            if "wechat_uid" in request.GET and int(request.GET["wechat_uid"]) in liked_users:
                m["liked"] = True
        else:
            meal = Meal(m["id"])
            meal.save()

    return JsonResponse(meals, safe = False)

def canteen_meal_detail(request, canteen_id, date, meal_id):
    # url = base_url + "/canteens/" + canteen_id + "/days/" + date + "/meals/" + meal_id
    # meal_info = requests.get(url).json()

    meal_info = {"status": 404, "message": "meal not found"}
    if int(meal_id) == 260:
        meal_info = {
                        "id": 260,
                        "name": "Gemüse-Couscouspfanne mit Joghurt-Ingwer-Dip, dazu bunter Blattsalat",
                        "notes": ["ovo-lacto-vegetabil", "mensaVital"],
                        "prices": {"students": 2.3, "employees": 3.65, "others": 4.6},
                        "category": "Alternativ-Angebot",
                        "likes": 0
                     }

    elif int(meal_id) == 10900:
        meal_info = {
                        "id": 10900,
                        "name": "Hähnchenschnitzel mit Brötchen",
                        "notes": [],
                        "prices": { "pupils": 2.4, "others": 4.3},
                        "category": "Cafeteria Heiße Theke",
                        "likes": 0
                     }

    meal_info["likes"] = 0
    meal_info["liked"] = False
    wechat_uid = 0
    liked_users = []
    updated = False
    result = MealQuery().get_meal(meal_id)

    if len(result):
        meal = result[0]
        liked_users = array.array('L', meal.liked_users).tolist()

        if "action" in request.GET and "wechat_uid" in request.GET:
            if request.GET["action"] == "like":
                if int(request.GET["wechat_uid"]) not in liked_users:
                    liked_users.append(int(request.GET["wechat_uid"]))
                    meal_info["liked"] = True

                    updated = True
            elif request.GET["action"] == "dislike":
                if int(request.GET["wechat_uid"]) in liked_users:
                    liked_users.remove(int(request.GET["wechat_uid"]))

                    updated = True

            if updated:
                meal.liked_users = array.array('L', liked_users)
                meal.update_data()

        meal_info["likes"] = len(liked_users)

    return JsonResponse(meal_info, safe = False)

def likes(request, canteen_id, date, meal_id):
    
    liked_users = []
    result = MealQuery().get_meal(meal_id)

    if len(result):
        meal = result[0]
        liked_users = array.array('L', meal.liked_users).tolist()

    return JsonResponse({"status": 200, "liked_users": liked_users}, safe = False)

