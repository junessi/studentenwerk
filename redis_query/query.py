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
    app_uid = app_prefix + user.id
    r.hmset(app_uid, user.toDict())


def find_user(uid):
    r = redis.Redis()
    user = RedisUser()
    app_uid = app_prefix + str(uid)
    uid = r.hget(app_uid, "id")
    if uid is not None:
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
