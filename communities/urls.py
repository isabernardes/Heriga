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
	url(r'^create/$', communities_create),
	url(r'^(?P<slug>[\w-]+)/$', communities_detail, name='detail'),
	url(r'^(?P<slug>[\w-]+)/edit$', communities_update, name='update'),
	url(r'^(?P<slug>[\w-]+)/delete/$', communities_delete),

]