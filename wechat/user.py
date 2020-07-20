from query.user import UserQuery
from django.http import JsonResponse
from datetime import datetime
import common.errors as errors

def get_user_info(request, user_id):
    users = UserQuery().get_user_info(user_id)

    if len(users):
        user = users[0]
        resp = user.dict()
        resp["last_commit_timestamp"] = int(datetime.timestamp(user.last_commit_timestamp))

    else:
        resp = errors.NotFound("User not found").dict()

    return JsonResponse(resp, safe = False)


