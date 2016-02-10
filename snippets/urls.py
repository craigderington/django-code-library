from django.conf.urls import url
from . import views, feed

urlpatterns = [
    url(r'^$', views.SnippetIndex.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='detail'),
    url(r'^feed/$', feed.LatestSnippets(), name='feed'),
]
