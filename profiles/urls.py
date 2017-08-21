from django.conf.urls import patterns, url

from .views import (
	profile_view,
	profile_update,
	#edit_info,
	#edit_jobs,
	#edit_qualifications,
	#edit_languages,
	#edit_pictures,
	#post_delete,
	
	)


urlpatterns = [
	
	url(r'^(?P<username>[\w.@+-]+)/$', profile_view, name='profile_view'),
	url(r'^(?P<username>[\w.@+-]+)/edit$', profile_update, name='profile_update'),
	#url(r'^(?P<username>[\w.@+-]+)/edit$', edit_info, name='edit_info'),
	#url(r'^(?P<username>[\w.@+-]+)/edit$', edit_jobs, name='edit_jobs'),
	#url(r'^(?P<username>[\w.@+-]+)/edit$', edit_qualifications, name='edit_qualifications'),
	#url(r'^(?P<username>[\w.@+-]+)/edit$', edit_languages, name='edit_languages'),
	#url(r'^(?P<username>[\w.@+-]+)/edit$', edit_pictures, name='edit_pictures'),
	#url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    ]