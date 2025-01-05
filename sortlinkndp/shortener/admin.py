from django.contrib import admin
from .models import ShortenedURL, URLVisit, SavedURL

@admin.register(ShortenedURL)
class ShortenedURLAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_url', 'created_at', 'clicks')
    search_fields = ('original_url', 'short_url')
    readonly_fields = ('clicks',)

@admin.register(SavedURL)
class SavedURLAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'saved_at', 'notes')
    search_fields = ('name', 'notes', 'url__short_url')
    list_filter = ('saved_at',)

@admin.register(URLVisit)
class URLVisitAdmin(admin.ModelAdmin):
    list_display = ('url', 'visited_at', 'ip_address')
    list_filter = ('visited_at',)
    search_fields = ('ip_address', 'user_agent', 'referrer')
