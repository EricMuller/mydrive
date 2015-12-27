from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
#from mysite.apps.notes import urls
from mysite import settings
from mysite import views


urlpatterns = [
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$',views.site),
	url(r'^infusion/', views.infusion),
    url(r'^digitalworld/', views.digitalworld),
    url(r'^bliss/', views.bliss),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^notes/', include('mysite.apps.notes.urls')),
    url(r'^photofolio/', include('mysite.apps.photofolio.urls')),
    url(r'^helios/', include('mysite.apps.helios.urls')),
    url(r'^prologue/', include('mysite.apps.prologue.urls')),
    url(r'^striped/', include('mysite.apps.striped.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
   # url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT },name="media"),
]


