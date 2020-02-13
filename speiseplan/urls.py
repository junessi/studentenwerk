from django.conf.urls import url
from django.urls import path, re_path
from speiseplan import views

urlpatterns = [
    path('canteens/', views.list_canteens),
    re_path(r'^canteens/(?P<canteen_id>[\d]+)/$', views.canteen_info),
    re_path(r'^canteens/(?P<canteen_id>[\d]+)/days$', views.canteen_dates),
    re_path(r'^canteens/(?P<canteen_id>[\d]+)/days/(?P<date>[\d]{4}-[\d]{2}-[\d]{2})/$', views.canteen_dates),
    re_path(r'^canteens/(?P<canteen_id>[\d]+)/days/(?P<date>[\d]{4}-[\d]{2}-[\d]{2})/meals/$', views.canteen_meals),
    re_path(r'^canteens/(?P<canteen_id>[\d]+)/days/(?P<date>[\d]{4}-[\d]{2}-[\d]{2})/meals/(?P<meal_id>[\d]+)/$', views.canteen_meal_detail),
]
