from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField

# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ('slug',)

class EntryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['title', 'slug', 'body', 'publish']}),
        ('Date Information', {'fields': ['created', 'modified'], 'classes': ['collapse']}),
        ('Tag Library', {'fields': ['tags']})
    ]
    list_display = ('title', 'created', 'modified')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}
    list_filter = ['created', 'publish']

# register the classes with the Admin site
admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Tag, TagAdmin)
