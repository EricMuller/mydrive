from django.conf.urls import include
from django.conf.urls import url

import django.views.defaults
# from mysite.apps.notes import urls
from mysite import views
from mysite import settings
import os
import sys

urlpatterns = [
    url(r'^drive/', include('drive.urls')),
    url(r'^mydrive/', include('mydrive.urls')),
    url(r'^$', views.site),
    # url(r'^404/$', django.views.defaults.page_not_found),
]

# Overrides the default 400 handler django.views.defaults.bad_request
#handler400 = 'mydrive.views.bad_request'
# Overrides the default 403 handler django.views.defaults.permission_denied
#handler403 = 'mydrive.views.permission_denied'
# Overrides the default 404 handler django.views.defaults.page_not_found
#handler404 = 'mydrive.views.page_not_found'
# Overrides the default 500 handler django.views.defaults.server_error
#handler500 = 'mydrive.views.server_error'

if settings.DEBUG:
    print('------------------------------------------------')
    print('PID:' + str(os.getpid()))
    print('PYTHON PATH:')
    for p in sys.path:
        print(p)
    print('------------------------------------------------')
