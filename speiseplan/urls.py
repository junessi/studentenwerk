from django.conf.urls import url
from speiseplan import views

urlpatterns = [
    url(r'^speiseplan/(?P<catering_name>[-\w]+)$', views.speise_plan),
]
