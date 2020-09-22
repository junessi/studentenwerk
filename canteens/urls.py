from django.conf.urls import url
from django.urls import path, re_path
from canteens import views

urlpatterns = [
    re_path(r'^$', views.list_canteens),
    re_path(r'^cache_meals$', views.cache_meals),
    re_path(r'^(?P<canteen_id>[\d]+)/$', views.canteen_info),
    re_path(r'^(?P<canteen_id>[\d]+)/days$', views.canteen_dates),
    re_path(r'^(?P<canteen_id>[\d]+)/days/(?P<date>[\d]{4}-[\d]{2}-[\d]{2})/$', views.canteen_date),
    re_path(r'^(?P<canteen_id>[\d]+)/days/(?P<date>[\d]{4}-[\d]{2}-[\d]{2})/meals/$', views.canteen_meals),
    re_path(r'^(?P<canteen_id>[\d]+)/days/(?P<date>[\d]{4}-[\d]{2}-[\d]{2})/meals/(?P<meal_id>[\d]+)/$', views.canteen_meal_detail),
    re_path(r'^(?P<canteen_id>[\d]+)/days/(?P<date>[\d]{4}-[\d]{2}-[\d]{2})/meals/(?P<meal_id>[\d]+)/likes$', views.likes),
    re_path(r'^(?P<canteen_id>[\d]+)/comments$', views.get_canteen_comments),
    re_path(r'^(?P<canteen_id>[\d]+)/addcomment/$', views.add_canteen_comment),
    re_path(r'^(?P<canteen_id>[\d]+)/cached_meals$', views.cached_meals),
]
