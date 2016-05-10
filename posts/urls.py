from django.conf.urls import patterns, url

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	tags,
	like_posts,
	)




urlpatterns = [
	url(r'^$', post_list, name='list'),
	url(r'^create/$', post_create, name='create'),
	url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
	url(r'^(?P<slug>[\w-]+)/edit$', post_update, name='update'),
	url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
	url(r'^tag/(?P<tag>\w+)/$', tags),
	url(r'^like/(?P<slug>[\w-]+)/$', like_posts),

    ]