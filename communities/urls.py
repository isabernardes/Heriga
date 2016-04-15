from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse

from .views import (
	communities_list,
	communities_create,
	communities_detail,
	communities_update,
	communities_delete,
	)


urlpatterns = [
	url(r'^$', communities_list, name='communities_list'),
	url(r'^create/$', communities_create, name='communities_create' ),
	url(r'^(?P<id>\d+)/$', communities_detail, name='detail'),
	url(r'^(?P<id>\d+)/edit/$', communities_update, name='update'),
	url(r'^(?P<id>\d+)/delete/$', communities_delete),

]