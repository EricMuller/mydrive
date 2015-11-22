from django.conf.urls import include, url
from mysite.apps.striped.views import index
from mysite.apps.striped.views import dispatch

urlpatterns = [
    url(r'^$', index),

    url(r'(?P<name>\w+)', dispatch),

]
