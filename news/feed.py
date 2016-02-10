from django.contrib.syndication.views import Feed
from .models import NewsStory

class LatestNews(Feed):
    title = 'Django and Python News'
    link = '/feed/'
    description = 'Latest Tech News for Python and Django'

    def items(self):
        return NewsStory.objects.published()[:10]
