from django.conf.urls import url
from speiseplan import views

urlpatterns = [
    url(r'^speiseplan/(?P<canteen_name>[-\w]+)$', views.canteen_details),
    url(r'^speiseplan/(?P<canteen_name>[-\w]+)/(?P<meal_query>[-\w]+)$', views.canteen_meals),
]
