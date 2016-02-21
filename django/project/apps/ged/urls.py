from django.conf.urls import url
from django.conf.urls import include
from ged import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'documents', views.DocumentViewSet)
router.register(r'baskets', views.BasketViewSet)
router.register(r'folders', views.FolderViewSet)
router.register(r'tree', views.TreeViewSet, base_name='tree')

# url(r'^apis/UploadFile/$', restviews.SnippetList.as_view(),name = 'UploadFile-list'),
# url(r'^apis/UploadFile/(?P<pk>[0-9]+)$', restviews.SnippetList.as_view(),name = 'UploadFile-detail'),
# print(router.urls)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
]
