from django.conf.urls import url
from speiseplan import views

urlpatterns = [
    url(r'^speiseplan/(?P<canteen_name>[-\w]+)$', views.canteen_details),
    url(r'^speiseplan/(?P<canteen_name>[-\w]+)/(?P<date_range>[-\w\[\],]*)$', views.canteen_meals),
]
