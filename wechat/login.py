from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from query.user import UserQuery, User
from redis_query.query import RedisUser
import wechat.error as error
import requests
import hashlib
import redis_query.query as RedisQuery

def verify_user(key, data, signature):
     buf = "{0}{1}".format(data, key)
     return signature == hashlib.sha1(buf.encode("utf-8")).hexdigest()

@csrf_exempt
def user_login(request):
    resp = error.NotFound().dict()
    APP_ID = settings.WECHAT_APP_ID
    APP_SECRET = settings.WECHAT_APP_SECRET

    if "code" in request.POST:
        resp = error.StatusOK().dict()
        code = request.POST["code"]
        api = "https://api.weixin.qq.com/sns/jscode2session"
        url = "{0}?appid={1}&secret={2}&js_code={3}&grant_type=authorization_code".format(api, APP_ID, APP_SECRET, code)

        result = requests.get(url)
        data = result.json()

        # init app user info
        resp["user"] = {
            "id": 0,
            "verified": False,
            "token": ""
        }

        session_key = ""
        if "session_key" in data:
            session_key = data["session_key"]

        # verify user's raw data and signature
        if "rawData" in request.POST and "signature" in request.POST:
            resp["user"]["verified"] = verify_user(session_key, request.POST["rawData"], request.POST["signature"])

        if "openid" in data:
            openid = data["openid"]

            user = User(openid)
            uq = UserQuery()
            if len(uq.get_user_by_openid(openid)) == 0:
                user.save()

            result = uq.get_user_by_openid(openid)
            if result:
                user = result[0] # get the first user
                resp["user"]["id"] = user.id
    else:
        resp["message"] = "code is not provided"

    return JsonResponse(resp)


