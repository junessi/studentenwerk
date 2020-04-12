from django.conf import settings
from django.db import models
from django.http import HttpResponse, JsonResponse
from query.user import UserQuery, User
import canteens.utils as utils
import wechat.error as error
import requests
import redis
import time

def user_login(request):
    resp = error.NotFound().dict()
    APP_ID = settings.WECHAT_APP_ID
    APP_SECRET = settings.WECHAT_APP_SECRET

    if "code" in request.GET:
        code = request.GET["code"]
        api = "https://api.weixin.qq.com/sns/jscode2session"
        url = "{0}?appid={1}&secret={2}&js_code={3}&grant_type=authorization_code".format(api, APP_ID, APP_SECRET, code)

        result = requests.get(url)
        data = result.json()

        if "openid" in data:
            openid = data["openid"]

            user = User(openid)
            uq = UserQuery()
            if len(uq.get_user_by_openid(openid)) == 0:
                user.save()

            result = uq.get_user_by_openid(openid)
            if result:
                user = result[0]
                resp = error.StatusOK().dict()
                resp["user"] = {"id": user.id}

    return JsonResponse(resp)

