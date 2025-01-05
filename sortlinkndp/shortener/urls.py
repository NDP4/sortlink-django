from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('saved/', views.saved_urls, name='saved_urls'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('<str:short_url>/stats/', views.stats, name='url_stats'),
    path('<str:short_url>/save/', views.save_url, name='save_url'),
    path('<str:short_url>/remove/', views.remove_saved_url, name='remove_saved_url'),
    path('<str:short_url>', views.redirect_to_original, name='redirect'),
]
