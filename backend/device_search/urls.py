from django.urls import path
from .views import DeviceSearchView

urlpatterns = [
    path('api/device-search/', DeviceSearchView.as_view(), name='device_search'),
]
