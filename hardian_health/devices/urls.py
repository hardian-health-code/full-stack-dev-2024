from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_device, name='search'),
    path('search/', views.search_device, name='search'),
    path('api/search/', views.api_search_device, name='api_search'),
]
