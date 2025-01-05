"""
URL configuration for sortlinkndp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shortener import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('saved/', views.saved_urls, name='saved_urls'),
    path('stats/<str:short_url>/', views.stats, name='url_stats'),
    path('stats/<str:short_url>/save/', views.save_url, name='save_url'),
    path('stats/<str:short_url>/remove/', views.remove_saved_url, name='remove_saved_url'),
    path('<str:short_url>/', views.redirect_to_original, name='redirect'),
]
