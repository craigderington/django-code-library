# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_snippet_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snippettag',
            options={'ordering': ['slug'], 'verbose_name': 'Snippet Tag', 'verbose_name_plural': 'Snippet Tags'},
        ),
    ]
