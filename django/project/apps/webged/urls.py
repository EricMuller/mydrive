from django.conf.urls import url
from webged.views import htmlviews
from webged.views import uploadviews

urlpatterns = [
    url(r'^test/', htmlviews.test),
    url(r'^login/', htmlviews.login),
    url(r'^partials/(?P<name>[-_\w]+)/(?P<name2>[-_\w]+)/(?P<name3>[-_\w]+)',
        htmlviews.partials3),
    url(r'^partials/(?P<name>[-_\w]+)/(?P<name2>[-_\w]+)',
        htmlviews.partials2),
    url(r'^partials/(?P<name>[-_\w]+)', htmlviews.partials),

    url(r'upload/', uploadviews.post),
    # ged/test
    url(r'(?P<name>\w+)', htmlviews.dispatch),
    url(r'^.*$', htmlviews.index),

]
