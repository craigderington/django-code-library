from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Job

# Create your tests here.

class JobPostTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='testuser')

    def test_create_unpublished_job(self):
        job = Job(job_title='My Test Title', job_description='', job_post_published=False)
        job.save()
        self.assertEqual(Job.objects.all().count(), 1)
        self.assetEqual(Job.objects.published().count(), 0)
        job.publish = True
        job.save()
        self.assertEqual(Job.objects.published().count(), 1)

class JobViewTest(TestCase):
    def test_job_feed_url(self):
        response = self.client.get('/feed/')
        self.assertIn('xml', response['Content-Type'])
