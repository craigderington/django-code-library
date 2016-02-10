from django.contrib import admin
from . import models


# Register your models here.
class NewsSourceAdmin(admin.ModelAdmin):
    list_display = ('source', 'source_ref')

class NewsStoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['news_title', 'story', 'slug', 'author', 'source_link', 'publish']}),
        ('Story Date',      {'fields': ['create_date', 'modify_date'], 'classes': ['collapse']}),
        ('Sources',         {'fields': ['source']})
    ]
    list_display = ('news_title', 'author', 'create_date')
    list_filter = ['create_date', 'publish']
    search_fields = ['news_title']

# Register model with admin site
admin.site.register(models.NewsStory, NewsStoryAdmin)
admin.site.register(models.NewsSource, NewsSourceAdmin)
