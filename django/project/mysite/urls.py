from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
# from mysite.apps.notes import urls
from mysite import views

urlpatterns = [
    url(r'^ged/apis/', include('ged.urls')),
    url(r'^ged/', include('webged.urls')),
    url(r'^$', views.site),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]
