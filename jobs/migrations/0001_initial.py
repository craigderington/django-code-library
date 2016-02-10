# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('job_title', models.CharField(help_text='Enter the job title.', max_length=50)),
                ('job_description', models.TextField(help_text='Enter the job description.')),
                ('job_company', models.CharField(help_text='Enter the company name.', max_length=50)),
                ('job_post_date', models.DateTimeField()),
                ('job_mod_date', models.DateTimeField()),
                ('job_post_end_date', models.DateTimeField()),
                ('job_post_publish_date', models.DateTimeField()),
                ('job_post_published', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
                'ordering': ['-job_post_date'],
            },
        ),
        migrations.CreateModel(
            name='JobContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('job_contact_name', models.CharField(help_text='Enter the job contact name.', max_length=50)),
                ('job_contact_email', models.EmailField(max_length=254)),
                ('job_contact_phone', models.CharField(max_length=15)),
                ('job_contact_phone_extension', models.CharField(help_text='Phone number extension', max_length=20)),
            ],
            options={
                'verbose_name': 'Job Contact',
                'verbose_name_plural': 'Job Contacts',
                'ordering': ['job_contact_name'],
            },
        ),
        migrations.CreateModel(
            name='JobRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('requirement', models.CharField(help_text='Enter the requirement name.', unique=True, max_length=50)),
                ('number_of_years', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Job Requirement',
                'verbose_name_plural': 'Job Requirements',
                'ordering': ['requirement'],
            },
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('job_type', models.CharField(help_text='Select Job Type', unique=True, max_length=20)),
            ],
            options={
                'verbose_name': 'Job Type',
                'verbose_name_plural': 'Job Types',
                'ordering': ['-job_type'],
            },
        ),
        migrations.AddField(
            model_name='job',
            name='job_contact',
            field=models.ForeignKey(to='jobs.JobContact'),
        ),
        migrations.AddField(
            model_name='job',
            name='job_require',
            field=models.ForeignKey(to='jobs.JobRequirement'),
        ),
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.ForeignKey(to='jobs.JobType'),
        ),
    ]
