"""
URL configuration for the predictor app.
"""
from django.urls import path
from . import views

urlpatterns = [
    # The home page of our app
    path('', views.predict_quality, name='predict_quality'),
]