from django.conf.urls import url
from . import views, feed

urlpatterns = [
    url(r'^$', views.BlogIndex.as_view(), name='index'),
    url(r'^(?P<slug>\S+)$', views.BlogDetail.as_view(), name='detail'),
    url(r'^feed/$', feed.LatestPosts(), name='feed'),
]
