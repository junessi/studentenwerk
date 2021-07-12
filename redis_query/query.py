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


prefix_app = "ddmensa_"
prefix_wechatuid = prefix_app + "wechat_uid_"
prefix_comment_canteenid = prefix_app + "comment_canteenid_"
MAX_COMMENTS_NUM = 10

def save_user(user):
    r = redis.Redis()
    app_uid = prefix_wechatuid + str(user.id)
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
    app_uid = prefix_wechatuid + str(uid)
    uid = r.hget(app_uid, "id")

    return uid != None

def find_user(uid):
    if user_exists(uid):
        r = redis.Redis()
        user = RedisUser()
        app_uid = prefix_wechatuid + str(uid)
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

def get_canteen_comments(cid, num = MAX_COMMENTS_NUM):
    try:
        r = redis.Redis()
        cid = int(cid)
        key = "{0}{1}".format(prefix_comment_canteenid, cid)
        if num < 1:
            num = MAX_COMMENTS_NUM

        comments = []
        for c in r.lrange(key, 0, num):
            comments.append(c.decode('utf-8'))

        return comments
    except:
        return []

def add_canteen_comment(cid, comment):
    try:
        r = redis.Redis()
        cid = int(cid)
        key = "{0}{1}".format(prefix_comment_canteenid, cid)
        r.lpush(key, comment)

        if r.llen(key) > MAX_COMMENTS_NUM:
            r.rpop(key)

        return True
    except:
        return False

def cache_meals(cid, meals, date):
    try:
        r = redis.Redis()
        key = "{0}{1}_canteenid_{2}_{3}".format(prefix_app, "cached_meals", cid, date)
        r.delete(key)
        for m in meals:
            r.lpush(key, m["id"])
        r.expire(key, 7*24*3600) # expire after a week
        return True
    except:
        return False

def has_cached_meals(cid, date):
    try:
        r = redis.Redis()
        key = "{0}{1}_canteenid_{2}_{3}".format(prefix_app, "cached_meals", cid, date)

        return r.exists(key)
    except:
        return False

def get_cached_meals(cid, date):
    try:
        r = redis.Redis()
        key = "{0}{1}_canteenid_{2}_{3}".format(prefix_app, "cached_meals", cid, date)
        return r.lrange(key, 0, -1)
    except:
        return []

def get_today():
    try:
        r = redis.Redis()
        return r.get("today")
    except:
        return ""
