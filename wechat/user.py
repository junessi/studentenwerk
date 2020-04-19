from django.db import models
from query.user import UserQuery
from speiseplan.models import Canteen, MealDate, Meal
from speiseplan.serializer import CanteenSerializer
from django.http import HttpResponse, JsonResponse
import canteens.utils as utils
import common.errors as errors

def get_user_info(request, user_id):
    users = UserQuery().get_user_info(user_id)

    if len(users):
        resp = [users[0].dict()]
    else:
        resp = errors.NotFound("User not found").dict()

    return JsonResponse(resp)


