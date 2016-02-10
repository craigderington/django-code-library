from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class JobRequirement(models.Model):
    requirement = models.CharField(max_length=50, unique=True, help_text='Enter the requirement name.')
    number_of_years = models.IntegerField()

    def __str__(self):
        return self.requirement

    class Meta:
        verbose_name = 'Job Requirement'
        verbose_name_plural = 'Job Requirements'
        ordering = ['requirement']


class JobContact(models.Model):
    job_contact_name = models.CharField(max_length=50, help_text='Enter the job contact name.')
    job_contact_email = models.EmailField()
    job_contact_phone = models.CharField(max_length=15)
    job_contact_phone_extension = models.CharField(max_length=20, help_text='Phone number extension')

    def __str__(self):
        return self.job_contact_name

    class Meta:
        verbose_name = 'Job Contact'
        verbose_name_plural = 'Job Contacts'
        ordering = ['job_contact_name']


class JobType(models.Model):
    job_type = models.CharField(max_length=20, unique=True, help_text='Select Job Type')

    def __str__(self):
        return self.job_type

    class Meta:
        verbose_name = 'Job Type'
        verbose_name_plural = 'Job Types'
        ordering = ['-job_type']

class JobQuerySet(models.QuerySet):
    def published(self):
        return self.filter(job_post_published=True)

class Job(models.Model):
    job_title = models.CharField(max_length=50, help_text='Enter the job title.')
    job_description = models.TextField(help_text='Enter the job description.')
    job_company = models.CharField(max_length=50, help_text='Enter the company name.')
    job_post_date = models.DateTimeField()
    job_mod_date = models.DateTimeField()
    job_post_end_date = models.DateTimeField()
    job_post_publish_date = models.DateTimeField()
    job_type = models.ForeignKey(JobType)
    job_require = models.ForeignKey(JobRequirement)
    job_contact = models.ForeignKey(JobContact)
    job_post_published = models.BooleanField(default=True)

    objects = JobQuerySet.as_manager()

    def __str__(self):
        return self.job_title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.get_object().id })

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
        ordering = ['-job_post_date']
