

from django.conf.urls import include, url
from mysite.apps.photofolio.views import index
from mysite.apps.photofolio.views import dispatch

urlpatterns = [
    url(r'^$', index),

    url(r'(?P<name>\w+)', dispatch),

]
