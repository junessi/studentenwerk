from django.conf.urls import url
from django.urls import path, re_path
from wechat import user, login

urlpatterns = [
    re_path(r'^user/login$', login.user_login),
    re_path(r'^user/(?P<user_id>[\d]+)/$', user.get_user_info),
    re_path(r'^user/checktoken/$', login.check_token)
]
