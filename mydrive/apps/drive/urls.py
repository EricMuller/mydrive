from django.conf.urls import url
from django.conf.urls import include
from drive import viewsets
from drive import settings
from rest_framework import routers
from rest_framework.authtoken import views
from django.contrib import admin
import rest_framework_swagger.urls


router = routers.DefaultRouter()
router.register(r'users', viewsets.UserViewSet)
router.register(r'groups', viewsets.GroupViewSet)
router.register(r'files', viewsets.FileViewSet)
router.register(r'baskets', viewsets.BasketViewSet)
router.register(r'nodes', viewsets.RepositoryViewSet)

apiRouter = routers.DefaultRouter()
apiRouter.register(
    r'(?P<username>[-_\w]+)/repositories', viewsets.DriveRepositoryViewSet,
    base_name='v1-repositories')
apiRouter.register(
    r'(?P<username>[-_\w]+)/tree', viewsets.DriveRepositoryAsTreeViewSet,
    base_name='v1-tree')
apiRouter.register(
    r'(?P<username>[-_\w]+)', viewsets.DriveViewSet,
    base_name='v1')


batchRouter = routers.DefaultRouter()
batchRouter.register(
    viewsets.BatchViewSet.url, viewsets.BatchViewSet,
    base_name='batch')

# import pdb   pdb.set_trace()

# url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
# router.register(r'plan', views.TreeViewSet.as_view(
        # {'post': 'create', 'get': 'list', 'delete': 'destroy'}), base_name='plan')
# url(r'^apis/UploadFile/$', restviews.SnippetList.as_view(),name = 'UploadFile-list'),
# url(r'^apis/UploadFile/(?P<pk>[0-9]+)$', restviews.SnippetList.as_view(),name = 'UploadFile-detail'),
# print(router.urls)

if settings.DEBUG:
    for u in router.urls:
        print(u)

urlpatterns = [
    url(r'^', include(router.urls, namespace='internal_apis')),
    url(r'^v1/', include(apiRouter.urls, namespace='external_apis')),
    url(r'^batchs/', include(batchRouter.urls, namespace='external_apis')),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^authentification/', views.obtain_auth_token),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include(rest_framework_swagger.urls)),
]
