from django.conf.urls import include, url
from mysite.apps.helios.views import index
from mysite.apps.helios.views import dispatch

urlpatterns = [
    url(r'^$', index),

    url(r'(?P<name>\w+)', dispatch),

]
