from django.conf.urls import patterns, include, url
from .views import *


urlpatterns = [
	url(r'^home/$', home),
]


