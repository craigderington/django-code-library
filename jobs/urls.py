from django.conf.urls import url
from . import views, feed

urlpatterns = [
    url(r'^$', views.JobIndex.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.JobDetail.as_view(), name='detail'),
    url(r'^feed/$', feed.LatestJobs(), name='feed'),
]
