from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import ShortenedURL, URLVisit, SavedURL
from django.urls import reverse
from django.db.models import Count
from django.db.models.functions import TruncDate
from datetime import timedelta
from django.utils import timezone
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re

def force_http(request):
    if request.is_secure():
        url = request.build_absolute_uri()
        url_http = url.replace('https://', 'http://', 1)
        return HttpResponseRedirect(url_http)
    return None

def get_website_title(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else None
        if title:
            # Clean and limit title length
            title = re.sub(r'[\n\t]', '', title.strip())
            return title[:200]
    except:
        return None
    return None

def home(request):
    # Force HTTP
    http_response = force_http(request)
    if http_response:
        return http_response

    if request.method == 'POST':
        original_url = request.POST.get('url')
        title = get_website_title(original_url)
        shortened_url = ShortenedURL.objects.create(
            original_url=original_url,
            title=title
        )
        return render(request, 'shortener/success.html', {
            'shortened': shortened_url,
            'scheme': 'http'
        })
    return render(request, 'shortener/home.html')

def redirect_to_original(request, short_url):
    # Force HTTP
    http_response = force_http(request)
    if http_response:
        return http_response

    url_object = get_object_or_404(ShortenedURL, short_url=short_url)
    
    # Track visit
    URLVisit.objects.create(
        url=url_object,
        ip_address=request.META.get('REMOTE_ADDR'),
        user_agent=request.META.get('HTTP_USER_AGENT'),
        referrer=request.META.get('HTTP_REFERER')
    )
    
    url_object.clicks += 1
    url_object.save()
    return redirect(url_object.original_url)

def stats(request, short_url):
    url_object = get_object_or_404(ShortenedURL, short_url=short_url)
    
    # Get daily visits for the last 30 days
    thirty_days_ago = timezone.now() - timedelta(days=30)
    daily_visits = url_object.visits.filter(
        visited_at__gte=thirty_days_ago
    ).annotate(
        date=TruncDate('visited_at')
    ).values('date').annotate(
        count=Count('id')
    ).order_by('date')

    # Get browser statistics
    browsers = url_object.visits.filter(
        user_agent__isnull=False
    ).values('user_agent').annotate(
        count=Count('id')
    ).order_by('-count')[:5]

    # Get recent visits
    recent_visits = url_object.visits.all()[:10]

    context = {
        'url': url_object,
        'daily_visits': list(daily_visits),
        'browsers': browsers,
        'recent_visits': recent_visits,
        'is_saved': SavedURL.objects.filter(url=url_object).exists()
    }
    return render(request, 'shortener/stats.html', context)

def save_url(request, short_url):
    if request.method == 'POST':
        url_object = get_object_or_404(ShortenedURL, short_url=short_url)
        name = request.POST.get('name', '')
        notes = request.POST.get('notes', '')
        
        # Check if already saved
        saved_url, created = SavedURL.objects.get_or_create(
            url=url_object,
            defaults={'name': name, 'notes': notes}
        )
        
        if not created:
            # Update existing
            saved_url.name = name
            saved_url.notes = notes
            saved_url.save()
        
        return JsonResponse({
            'success': True,
            'message': 'URL berhasil disimpan!'
        })
    return JsonResponse({'success': False}, status=400)

def remove_saved_url(request, short_url):
    if request.method == 'POST':
        url_object = get_object_or_404(ShortenedURL, short_url=short_url)
        SavedURL.objects.filter(url=url_object).delete()
        return JsonResponse({
            'success': True,
            'message': 'URL berhasil dihapus dari simpanan!'
        })
    return JsonResponse({'success': False}, status=400)

def saved_urls(request):
    saved = SavedURL.objects.all().select_related('url')
    return render(request, 'shortener/saved_urls.html', {
        'saved_urls': saved
    })

def privacy(request):
    return render(request, 'shortener/privacy.html')

def terms(request):
    return render(request, 'shortener/terms.html')
