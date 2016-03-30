from django.conf.urls import url
from django.conf.urls import include
from backdrive import viewsets
from rest_framework import routers
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'users', viewsets.UserViewSet)
router.register(r'groups', viewsets.GroupViewSet)
router.register(r'documents', viewsets.DocumentViewSet)
router.register(r'baskets', viewsets.BasketViewSet)
router.register(r'folders', viewsets.FolderViewSet)
router.register(r'plan', viewsets.TreeViewSet, base_name='plan')

# router.register(
#     r'authentification',
#     AuthentificationViewSet, base_name='authentification')

# url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
#router.register(r'plan', views.TreeViewSet.as_view({'post': 'create', 'get': 'list', 'delete': 'destroy'}), base_name='plan')

# url(r'^apis/UploadFile/$', restviews.SnippetList.as_view(),name = 'UploadFile-list'),
# url(r'^apis/UploadFile/(?P<pk>[0-9]+)$', restviews.SnippetList.as_view(),name = 'UploadFile-detail'),
print(router.urls)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^authentification/', views.obtain_auth_token)
]
