from django.views import generic
from . import models

# Create your views here.

class JobIndex(generic.ListView):
    queryset = models.Job.objects.published()
    template_name = 'job_list.html'
    paginate_by = 20

class JobDetail(generic.DetailView):
    model = models.Job
    template_name = 'job_detail.html'
