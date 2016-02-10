from django.contrib.syndication.views import Feed
from .models import Job

class LatestJobs(Feed):
    title = 'Django Job Listings'
    link = '/feed/'
    description = 'Latest Job Postings for Django and Python'

    def items(self):
        return Job.objects.published()[:10]
