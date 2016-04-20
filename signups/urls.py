from django.conf.urls import patterns, include, url
#from django.core.urlresolvers import reverse
from .views import *

#from .views import (
#	SignUp,
#	)

urlpatterns = [
#	url(r'^$', SignUp, name='signup'),
	url(r'^register/success/$', register_success),
	url(r'^home/$', home),
]


