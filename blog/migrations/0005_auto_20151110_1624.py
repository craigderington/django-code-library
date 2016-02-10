# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151109_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='entry',
            name='modified',
            field=models.DateTimeField(),
        ),
    ]
