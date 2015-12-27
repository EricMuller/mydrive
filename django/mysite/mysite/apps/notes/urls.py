from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from rest_framework import routers
from mysite.apps.notes import views
#from mysite.apps.notes.views import home
from mysite.apps.notes.views import index

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'notes', views.NoteViewSet)
router.register(r'restnotes', views.ReSTNoteViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^apis/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', index),
]