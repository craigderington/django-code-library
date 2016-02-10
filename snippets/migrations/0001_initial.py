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
            name='Snippet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('snippet_title', models.CharField(help_text='Limit your snippet titles to 200 characters.', max_length=200)),
                ('snippet_body', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField()),
                ('publish', models.BooleanField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Python Snippet',
                'verbose_name_plural': 'Python Snippets',
                'ordering': ['-create_date'],
            },
        ),
        migrations.CreateModel(
            name='SnippetTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='snippet',
            name='snippet_tags',
            field=models.ManyToManyField(to='snippets.SnippetTag'),
        ),
    ]
