# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20151112_1811'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newssource',
            options={'verbose_name_plural': 'News Sources', 'verbose_name': 'News Source'},
        ),
    ]
