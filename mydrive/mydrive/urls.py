from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
# from mysite.apps.notes import urls
from mydrive import views

urlpatterns = [
    url(r'^mydrive/apis/', include('backdrive.urls')),
    url(r'^mydrive/', include('webdrive.urls')),
    url(r'^$', views.site),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]
