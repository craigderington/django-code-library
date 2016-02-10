# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='source_link',
            field=models.URLField(default='google.com'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newssource',
            name='source',
            field=models.CharField(max_length=200, help_text='Source of the News Article'),
        ),
        migrations.AlterField(
            model_name='newsstory',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, help_text='News Story URL Path'),
        ),
    ]
