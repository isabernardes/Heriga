from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from posts.views import *
from profiles.views import *
from signups.views import *

urlpatterns = [
  
    #url(r'^admin/', admin.site.urls),
    url(r'^$', 'signups.views.home', name='homepage'),
    url(r'^contact-us/$','signups.views.contactus', name='contactus'),
    url(r'^posts/', include('posts.urls', namespace='posts')),
    url(r'^communities/', include('communities.urls', namespace='communities')),
    url(r'^signups/$', 'signups.views.register', name='signup'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'signups.views.logout_page', name='logout'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/success/$', register_success),
    url(r'^comments/', include('comments.urls', namespace='comments')),
    url(r'^profile/', include('profiles.urls', namespace='profile')),
    url(r'^test/$', 'posts.views.post_profile', name='post_profile'),

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

