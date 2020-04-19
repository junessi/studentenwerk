import redis

class RedisUser:
    def __init__(self):
        self.id = 0
        self.openid = ""
        self.session_key = ""
        self.raw_data = ""
        self.signature = ""
        self.token = ""

    def toDict(self):
        return {
            "id": self.id,
            "openid": self.openid,
            "session_key": self.session_key,
            "raw_data": self.raw_data,
            "signature": self.signature,
            "token": self.token
        }


app_prefix = "ddmensa_wechat_uid_"

def save_user(user):
    r = redis.Redis()
    app_uid = app_prefix + str(user.id)
    if user.id:
        r.hset(app_uid, "id", user.id)

    if user.openid:
        r.hset(app_uid, "openid", user.openid)

    if user.session_key:
        r.hset(app_uid, "session_key", user.session_key)

    if user.raw_data:
        r.hset(app_uid, "raw_data", user.raw_data)

    if user.signature:
        r.hset(app_uid, "signature", user.signature)

    if user.token:
        r.hset(app_uid, "token", user.token)

def user_exists(uid):
    r = redis.Redis()
    app_uid = app_prefix + str(uid)
    uid = r.hget(app_uid, "id")

    return uid != None

def find_user(uid):
    if user_exists(uid):
        r = redis.Redis()
        user = RedisUser()
        app_uid = app_prefix + str(uid)
        uid = r.hget(app_uid, "id")
        user.id = int(uid)

        openid = r.hget(app_uid, "openid")
        if openid is not None:
            user.openid = openid.decode("utf-8")

        session_key = r.hget(app_uid, "session_key")
        if session_key is not None:
            user.session_key = session_key.decode("utf-8")

        raw_data = r.hget(app_uid, "raw_data")
        if raw_data is not None:
            user.raw_data = raw_data.decode("utf-8")

        signature = r.hget(app_uid, "signature")
        if signature is not None:
            user.signature = signature.decode("utf-8")

        token = r.hget(app_uid, "token")
        if token is not None:
            user.token = token.decode("utf-8")

        return user

    return None

def verify_token(uid, token):
    user = find_user(uid)
    if user is not None and user.token == token:
        return True

    return False

