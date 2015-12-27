from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from rest_framework import routers
from mysite.apps.notes.views import restviews
from mysite.apps.notes.views import htmlviews
#from mysite.apps.notes.views import home
#from mysite.apps.notes.views.htmlviews import index

router = routers.DefaultRouter()
router.register(r'users', restviews.UserViewSet)
router.register(r'groups', restviews.GroupViewSet)
router.register(r'notes', restviews.NoteViewSet)
router.register(r'restnotes', restviews.ReSTNoteViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.

urlpatterns = [
    url(r'^apis/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', htmlviews.index),
]

#def get_urls(self):
#    return urlpatterns