from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse

from .views import (
	SignUp,
	)

urlpatterns = [
	url(r'^$', SignUp, name='signup'),


]