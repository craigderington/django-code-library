from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import NewsStory

# Create your tests here.

class NewsStoryTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='testuser')

    def test_create_unpublished_newsstory(self):
        news = Job(news_title='My Test Title', story='this', publish=False)
        news.save()
        self.assertEqual(NewsStory.objects.all().count(), 1)
        self.assetEqual(NewsStory.objects.published().count(), 0)
        news.publish = True
        news.save()
        self.assertEqual(NewsStory.objects.published().count(), 1)

class NewsStoryViewTest(TestCase):
    def test_news_feed_url(self):
        response = self.client.get('/feed/')
        self.assertIn('xml', response['Content-Type'])
