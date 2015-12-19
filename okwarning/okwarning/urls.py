from django.conf.urls import url, include
from django.contrib import admin

from okwarning.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^/', HomeView.as_view(), name='home'),
    url(r'^new/', NewWarningTemplateView.as_view(), name='new'),

    url(r'^', include([
        url(r'^facebook/$', FacebookPageRedirectView.as_view(), name='page'),
        url(r'^facebook/message/$', FacebookMessageRedirectView.as_view(), name='message'),
        url(r'^contact/$', FacebookMessageRedirectView.as_view(), name='contact'),
    ], namespace='facebook')),
]
