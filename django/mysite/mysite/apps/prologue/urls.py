from django.conf.urls import include, url
from mysite.apps.prologue.views import index
from mysite.apps.prologue.views import dispatch

urlpatterns = [
    url(r'^$', index),

    url(r'(?P<name>\w+)', dispatch),

]
