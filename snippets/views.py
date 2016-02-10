from django.views import generic
from . import models

# Create your views here.

class SnippetIndex(generic.ListView):
    queryset = models.Snippet.objects.all()
    template_name = 'snippet_list.html'
    paginate_by = 25

class SnippetDetail(generic.DetailView):
    model = models.Snippet
    template_name = 'snippet_detail.html'
