from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from query.user import UserQuery, User
from redis_query.query import RedisUser
import common.errors as errors
import requests
import hashlib
import secrets
import redis_query.query as RedisQuery

def verify_user(key, data, signature):
     buf = "{0}{1}".format(data, key)
     return signature == hashlib.sha1(buf.encode("utf-8")).hexdigest()

def generate_token():
    return secrets.token_hex(32)

@csrf_exempt
def user_login(request):
    resp = errors.NotFound().dict()
    APP_ID = settings.WECHAT_APP_ID
    APP_SECRET = settings.WECHAT_APP_SECRET

    if "code" in request.POST:
        resp = errors.StatusOK().dict()
        code = request.POST["code"]
        api = "https://api.weixin.qq.com/sns/jscode2session"
        url = "{0}?appid={1}&secret={2}&js_code={3}&grant_type=authorization_code".format(api, APP_ID, APP_SECRET, code)

        result = requests.get(url)
        data = result.json()
        # data = { "openid": "test_openid", "session_key": "fake session key" }

        # init app user info
        resp["user"] = {
            "id": 0,
            "verified": False,
            "token": ""
        }

        session_key = ""
        raw_data = ""
        signature = ""

        if "session_key" in data:
            session_key = data["session_key"]

        # verify user's raw data and signature
        if "rawData" in request.POST and "signature" in request.POST:
            raw_data = request.POST["rawData"]
            signature = request.POST["signature"]
            resp["user"]["verified"] = verify_user(session_key, raw_data, signature)

        if "openid" in data:
            openid = data["openid"]

            user = User(openid=openid)
            uq = UserQuery()
            if len(uq.get_user_by_openid(openid)) == 0:
                user.save()

            result = uq.get_user_by_openid(openid)
            if result:
                user = result[0] # get the first user
                user_id = user.id

                # create or replace user info in redis
                ru = RedisUser()
                ru.id = user_id
                ru.openid = openid
                ru.session_key = session_key
                ru.raw_data = raw_data
                ru.signature = signature
                ru.token = generate_token() # generate new token
                RedisQuery.save_user(ru)

                resp["user"]["token"] = ru.token
                resp["user"]["id"] = user_id
    else:
        resp["message"] = "code is not provided"

    return JsonResponse(resp)

@csrf_exempt
def check_token(request):
    if {"wechat_uid", "token"} <= set(request.POST):
        try:
            uid = int(request.POST["wechat_uid"])
            if uid < 1:
                raise Exception("invalid wechat uid")
            token = request.POST["token"] 

            if RedisQuery.verify_token(uid, token) == False:
                return JsonResponse(errors.InvalidToken().dict(), safe = False)

            return JsonResponse(errors.StatusOK("OK").dict(), safe = False)
        except Exception as e:
            return JsonResponse(errors.StatusError(str(e)).dict(), safe = False)


    return JsonResponse(errors.InvalidToken().dict(), safe = False)
