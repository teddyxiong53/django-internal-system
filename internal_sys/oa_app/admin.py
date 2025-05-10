from django.contrib import admin
from .models import Announcement

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date')
    list_filter = ('publish_date', 'author')
    search_fields = ('title', 'content')
    date_hierarchy = 'publish_date'

admin.site.register(Announcement, AnnouncementAdmin)
