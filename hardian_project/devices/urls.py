from django.urls import path, include
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('search/', permanent=False)),
    path('search/', views.search_view, name='search_view'),
    path('api/search/', views.api_search_view, name='api_search_view'),
]