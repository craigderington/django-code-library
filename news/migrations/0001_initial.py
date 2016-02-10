# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsSource',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('source', models.CharField(max_length=200, help_text='Source of the News Article')),
                ('source_ref', models.URLField()),
            ],
            options={
                'verbose_name': 'News Source',
                'verbose_name_plural': 'News Sources',
            },
        ),
        migrations.CreateModel(
            name='NewsStory',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('news_title', models.CharField(max_length=200, help_text='News Story Title')),
                ('slug', models.SlugField(unique=True, max_length=200, help_text='News Story URL Path')),
                ('story', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField()),
                ('source_link', models.URLField()),
                ('publish', models.BooleanField()),
                ('author', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
                ('source', models.ManyToManyField(to='news.NewsSource')),
            ],
            options={
                'verbose_name': 'News Story',
                'verbose_name_plural': 'News Stories',
                'ordering': ['-create_date'],
            },
        ),
    ]
