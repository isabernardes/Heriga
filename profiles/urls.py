from django.conf.urls import patterns, url

from .views import (
	profile_detail,
	profile_update,
	#post_delete,
	
	)




urlpatterns = [
	
	url(r'^(?P<username>[\w.@+-]+)/$', profile_detail, name='profile_detail'),
	url(r'^(?P<username>[\w.@+-]+)/edit$', profile_update, name='profile_update'),
	#url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    ]