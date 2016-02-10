from django.contrib.syndication.views import Feed
from .models import Snippet

class LatestSnippets(Feed):
    title = 'Python and Django Code Snippet Library'
    link = '/feed/'
    description = 'Latest Code Snippets for Python and Django'

    def items(self):
        return Snippet.objects.published()[:10]
