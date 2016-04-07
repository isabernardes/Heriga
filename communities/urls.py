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
	url(r'^$', communities, name='communities_list'),
	url(r'^create/$', communities_create),
	url(r'^update/$', communities_detail, name='detail'),
	url(r'^edit/$', communities_update, name='update'),
	url(r'^delete/$', communities_delete),

]