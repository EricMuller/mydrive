from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

from mysite.views import hello
from mysite.views import note
from mysite.views import infusion
from mysite.views import digitalworld
from mysite.views import bliss
#from mysite.apps.notes.views import home
#from mysite.apps.notes.views import index
#from mysite.apps.notes.views import home
#from mysite.apps.notes.views import index
from mysite import settings


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'mysite.apps.notes.views.home', name='home'),
	url(r'^infusion/', infusion),
    url(r'^digitalworld/', digitalworld),
    url(r'^bliss/', bliss),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^notes/', include('mysite.apps.notes.urls')),
    url(r'^photofolio/', include('mysite.apps.photofolio.urls')),
    url(r'^helios/', include('mysite.apps.helios.urls')),
    url(r'^prologue/', include('mysite.apps.prologue.urls')),
    url(r'^striped/', include('mysite.apps.striped.urls')),

   # url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT },name="media"),
    #url(r'^hello/$', hello),
    #url(r'^', index),
    
    #url(r'^note/(\d{1,2})/$', note),

]
