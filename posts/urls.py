from django.conf.urls import patterns, url

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	tags,
	#post_profile,
	user,
	PostLikeToggle,
	PostLikeAPIToggle,
	)

urlpatterns = [
	url(r'^$', post_list, name='list'),
	url(r'^create/$', post_create, name='create'),
	url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
	url(r'^(?P<slug>[\w-]+)/like/$', PostLikeToggle.as_view(), name='like-toggle'),
	url(r'^api/(?P<slug>[\w-]+)/like/$', PostLikeAPIToggle.as_view(), name='like-api-toggle'),
	url(r'^(?P<slug>[\w-]+)/edit$', post_update, name='update'),
	url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
	url(r'^tag/(?P<tag>\w+)/$', tags),
	url(r'^$', user, name='list'),
	#url(r'^post_profile/$', post_profile, name='post_profile'),

	

    ]