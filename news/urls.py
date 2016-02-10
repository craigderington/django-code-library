from django.conf.urls import url
from . import views, feed

urlpatterns = [
    url(r'^$', views.NewsIndex.as_view(), name='index'),
    url(r'^(?P<slug>\S+)$', views.NewsDetail.as_view(), name='detail'),
    url(r'^feed/$', feed.LatestNews(), name='feed'),
]
