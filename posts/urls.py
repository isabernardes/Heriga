from django.conf.urls import patterns, url
from posts import views

urlpatterns = [
	url(r'^$', "posts.views.posts_home"),

]