from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'posts.views.home', name='homepage'),
    url(r'^about-us/$','posts.views.aboutus', name='aboutus'),
    url(r'^posts/', include('posts.urls', namespace='posts')),
    url(r'^communities/$', 'communities.views.communities', name='communities'),
    url(r'^signups/$', 'signups.views.SignUp', name='signup'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)