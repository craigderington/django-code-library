from django.contrib.syndication.views import Feed
from .models import Entry

class LatestPosts(Feed):
    title = 'Intro to Python and Django'
    link = '/feed/'
    description = 'Latest Posts from Python and Django'

    def items(self):
        return Entry.objects.published()[:10]
