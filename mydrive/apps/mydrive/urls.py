from django.conf.urls import url
from mydrive import views
from mydrive import upload

urlpatterns = [
    url(r'^test/', views.test),
    url(r'^login/', views.login),
    url(r'^partials/(?P<name>[-_\w]+)/(?P<name2>[-_\w]+)/(?P<name3>[-_\w]+)',
        views.partials3),
    url(r'^partials/(?P<name>[-_\w]+)/(?P<name2>[-_\w]+)',
        views.partials2),
    url(r'^partials/(?P<name>[-_\w]+)', views.partials),
    # url(r'(?P<name>\w+)', views.dispatch),
    url(r'upload/', upload.post),
    url(r'index^.*$', views.index),
    url(r'^.*$', views.index),

]
