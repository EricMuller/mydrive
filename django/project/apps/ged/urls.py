from django.conf.urls import url
from django.conf.urls import include

from rest_framework import routers
from ged.views import restviews


router = routers.DefaultRouter()
router.register(r'users', restviews.UserViewSet)
router.register(r'groups', restviews.GroupViewSet)
router.register(r'documents', restviews.DocumentViewSet)
router.register(r'baskets', restviews.BasketViewSet)

# url(r'^apis/UploadFile/$', restviews.SnippetList.as_view(),name = 'UploadFile-list'),
# url(r'^apis/UploadFile/(?P<pk>[0-9]+)$', restviews.SnippetList.as_view(),name = 'UploadFile-detail'),
# print(router.urls)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
]
