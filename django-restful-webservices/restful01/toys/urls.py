from django.conf.urls import url

from .views import toy_detail, toy_list

urlpatterns = [
    url(r'^toys/$', toy_list),
    url(r'^toys/(?P<pk>[0-9]+)$', toy_detail),
]
