from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

class NewsSource(models.Model):
    source = models.CharField(max_length=200, help_text='Source of the News Article')
    source_ref = models.URLField()

    def __str__(self):
        return self.source

    class Meta:
        verbose_name = 'News Source'
        verbose_name_plural = 'News Sources'


class NewsQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class NewsStory(models.Model):
    news_title = models.CharField(max_length=200, help_text='News Story Title')
    slug = models.SlugField(max_length=200, unique=True, help_text='News Story URL Path')
    author = models.ForeignKey(User, null=True, blank=True)
    story = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField()
    source = models.ManyToManyField(NewsSource)
    source_link = models.URLField()
    publish = models.BooleanField()

    objects = NewsQuerySet.as_manager()

    def __str__(self):
        return self.news_title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug':self.slug })

    class Meta:
        verbose_name = 'News Story'
        verbose_name_plural = 'News Stories'
        ordering = ['-create_date']
