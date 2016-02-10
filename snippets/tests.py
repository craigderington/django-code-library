from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Snippet

# Create your tests here.

class SnippetTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='testuser')

    def test_create_unpublished_snippet(self):
        snippet = Snippet(title='My Test Snipet', body='', publish=False)
        snippet.save()
        self.assertEqual(Snippet.objects.all().count(), 1)
        self.assetEqual(Snippet.objects.published().count(), 0)
        snippet.publish = True
        snippet.save()
        self.assertEqual(Snippet.objects.published().count(), 1)

class SnippetViewTest(TestCase):
    def test_snippet_feed_url(self):
        response = self.client.get('/feed/')
        self.assertIn('xml', response['Content-Type'])
