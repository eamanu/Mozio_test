from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *


urlpatterns = {
    url(r'^providers/v1/list/$', ListView.as_view(), name="list"),
    url(r'^providers/v1/create/$', CreateView.as_view(), name="create"),
    url(r'^providers/v1/update/$', UpdateView.as_view(), name="update"),
    url(r'^providers/v1/delete/$', DeleteView.as_view(), name="delete")
}

urlpatterns = format_suffix_patterns(urlpatterns)
