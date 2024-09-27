from django.urls import path

from . import views

urlpatterns = [
    path("", views.search_device, name="search_device"),
    path("v1/device/", views.api_search_device, name="api_search_device"),
]
