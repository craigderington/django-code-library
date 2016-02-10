from django.views import generic
from . import models

# Create your views here.

class NewsIndex(generic.ListView):
    queryset = models.NewsStory.objects.published()
    template = 'news_list.html'
    paginate_by = 10

class NewsDetail(generic.DetailView):
    model = models.NewsStory
    template = 'news_detail.html'
