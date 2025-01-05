from django.db import models
import random
import string
from django.utils.text import slugify

def generate_short_url(title=None):
    if title:
        # Create a slug from title and take first 4 characters
        slug = slugify(title)[:4]
        # Add 2 random characters
        random_chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=2))
        return f"{slug}{random_chars}"
    else:
        characters = string.ascii_letters + string.digits
        return ''.join(random.choices(characters, k=6))

class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=6, unique=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = generate_short_url(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.original_url} -> {self.short_url}"

class URLVisit(models.Model):
    url = models.ForeignKey(ShortenedURL, on_delete=models.CASCADE, related_name='visits')
    visited_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    referrer = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ['-visited_at']

class SavedURL(models.Model):
    url = models.ForeignKey(ShortenedURL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    saved_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ['-saved_at']

    def __str__(self):
        return f"{self.name} - {self.url.short_url}"
