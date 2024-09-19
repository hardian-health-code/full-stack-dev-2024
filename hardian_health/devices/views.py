from .models import FdaData, EudamedData
from django.shortcuts import render
from django.http import JsonResponse

def search_device(request):
    query = request.GET.get('device_name')
    fda_result = FdaData.objects.filter(device_name__iexact=query).first()
    eudamed_result = EudamedData.objects.filter(device_name__iexact=query).first()

    not_found_in_both = not fda_result and not eudamed_result

    return render(request, 'devices/search_results.html', {
        'fda_result': fda_result,
        'eudamed_result': eudamed_result,
        'query': query,
        'not_found_in_both': not_found_in_both,
    })

def api_search_device(request):
    query = request.GET.get('device_name')
    fda_result = FdaData.objects.filter(device_name__iexact=query)
    eudamed_result = EudamedData.objects.filter(device_name__iexact=query)

    return JsonResponse({
        'fda_data': list(fda_result.values()),
        'eudamed_data': list(eudamed_result.values())
    })