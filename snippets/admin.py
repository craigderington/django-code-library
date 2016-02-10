from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField

# Register your models here.

class SnippetTagAdmin(admin.ModelAdmin):
    list_display = ('slug',)

class SnippetAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['snippet_title', 'snippet_body', 'author', 'publish']}),
        ('Date Information', {'fields': ['modified_date'], 'classes': ['collapse']}),
        ('Tag Library', {'fields': ['snippet_tags']})
    ]
    list_display = ('snippet_title', 'author', 'create_date', 'modified_date')
    search_fields = ['snippet_title']
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}
    list_filter = ['create_date', 'publish']

# register the classes with the Admin site
admin.site.register(models.Snippet, SnippetAdmin)
admin.site.register(models.SnippetTag, SnippetTagAdmin)
