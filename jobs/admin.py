from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField


# Register your models here.

class JobRequirementAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,    {'fields': ['requirement', 'number_of_years']})
    ]
    list_display = ('requirement', 'number_of_years')
    list_filter = ['requirement']
    search_fields = ['requirement']


class JobContactAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['job_contact_name', 'job_contact_email', 'job_contact_phone', 'job_contact_phone_extension']})
    ]
    list_display = ('job_contact_name', 'job_contact_email', 'job_contact_phone')
    list_filter = ['job_contact_name']
    search_fields = ['job_contact_name']

class JobTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['job_type']})
    ]
    list_display = ('job_type',)
    list_filter = ['job_type']
    search_fields = ['job_type']

class JobAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['job_type', 'job_title', 'job_description', 'job_company', 'job_contact', 'job_require']}),
        ('Job Dates',   {'fields':['job_post_date', 'job_mod_date', 'job_post_end_date']}),
        ('Job Published', {'fields':['job_post_published', 'job_post_publish_date']})
    ]
    list_display = ('job_title', 'job_company', 'job_post_date', 'job_contact')
    list_filter = ['job_post_date']
    search_fields = ['job_title']


# Register model with admin site
admin.site.register(models.JobRequirement, JobRequirementAdmin)
admin.site.register(models.JobContact, JobContactAdmin)
admin.site.register(models.JobType, JobTypeAdmin)
admin.site.register(models.Job, JobAdmin)
