from django.conf.urls import url
from webged.views import htmlviews
from webged.views import uploadviews

urlpatterns = [
    url(r'^test/', htmlviews.test),
    url(r'^partials/(?P<name>[-_\w]+)', htmlviews.partials),
    url(r'upload/', uploadviews.post),
    # ged/test
    url(r'(?P<name>\w+)', htmlviews.dispatch),
    url(r'^.*$', htmlviews.index),

]
