from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from .models import FDAData, EudamedData
import json

# functions for data cleaning

# Normalize the device name.
def clean_device_name(name):
    return name.strip().lower()

#Remove duplicates from the device list based on the device name.
def remove_duplicates(devices, key='device_name'):
    unique_devices = {device[key]: device for device in devices}.values()
    return list(unique_devices)

# Get device data based on search parameter
def get_search_data(device_name):
    cleaned_device_name = clean_device_name(device_name)
    
    # Fetch and clean FDA data
    fda_devices = list(FDAData.objects.all().values())
    cleaned_fda_devices = [
        {**device, 'device_name': clean_device_name(device['device_name'])}
        for device in fda_devices
    ]
    
    # Fetch and clean Eudamed data
    eudamed_devices = list(EudamedData.objects.all().values())
    cleaned_eudamed_devices = [
        {**device, 'device_name': clean_device_name(device['device_name'])}
        for device in eudamed_devices
    ]
    
    # Find matching devices
    matched_fda_devices = [device for device in cleaned_fda_devices if device['device_name'] == cleaned_device_name]
    matched_eudamed_devices = [device for device in cleaned_eudamed_devices if device['device_name'] == cleaned_device_name]

    # If no search term is provided, return all cleaned data
    if not cleaned_device_name:
        matched_fda_devices = cleaned_fda_devices
        matched_eudamed_devices = cleaned_eudamed_devices

    # Remove duplicates based on device_name
    matched_fda_devices = remove_duplicates(matched_fda_devices)
    matched_eudamed_devices = remove_duplicates(matched_eudamed_devices)

    response_data = {
        'fda_devices': matched_fda_devices,
        'eudamed_devices': matched_eudamed_devices,
        'fda_not_found': not matched_fda_devices,
        'eudamed_not_found': not matched_eudamed_devices,
        'not_found': not matched_fda_devices and not matched_eudamed_devices,
        'fda_columns': list(cleaned_fda_devices[0].keys()) if cleaned_fda_devices else [],
        'eudamed_columns': list(cleaned_eudamed_devices[0].keys()) if cleaned_eudamed_devices else [],
    }
    return response_data

# Create your views here.

# bonus task for API Endpoint
def api_search_view(request):
    device_name = request.GET.get('device_name', '').strip()
    response_data = get_search_data(device_name)

    return JsonResponse(response_data, encoder=DjangoJSONEncoder)

# search view
def search_view(request):
    device_name = request.GET.get('device_name', '').strip()
    response_data = get_search_data(device_name)

    return render(request, 'search_results.html', response_data)


