"""
Main URL configuration for the wine_predictor project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('predictor.urls')), # Include URLs from our predictor app
]
