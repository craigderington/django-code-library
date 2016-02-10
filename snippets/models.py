from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class SnippetTag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Snippet Tag'
        verbose_name_plural = 'Snippet Tags'
        ordering = ['slug']

class Snippet(models.Model):
    snippet_title = models.CharField(max_length=200, help_text='Limit your snippet titles to 200 characters.')
    snippet_body = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField()
    publish = models.BooleanField()
    snippet_tags = models.ManyToManyField(SnippetTag)
    author = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return self.snippet_title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.get_object().id})

    class Meta:
        verbose_name = 'Python Snippet'
        verbose_name_plural = 'Python Snippets'
        ordering = ['-create_date']
