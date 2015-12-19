from django.conf.urls import url
from django.contrib import admin

from okwarning.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', HomeView.as_view(), name='home'),
    url(r'^new/', NewWarningTemplateView.as_view(), name='new'),
]
