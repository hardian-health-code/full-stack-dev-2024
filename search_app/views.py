from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import EudamedData, FDAData


def search_device(request):
    query = request.GET.get("q", "")
    fda_results, eudamed_results = None, None
    not_found_message = ""

    if query:
        fda_results = FDAData.objects.get_distinct_device_names().filter(
            device_name__iexact=query
        )
        eudamed_results = (
            EudamedData.objects.get_distinct_device_names().
            filter(device_name__iexact=query)
        )
        if not fda_results.exists():
            not_found_message = "Device not found in FDA data."
        if not eudamed_results.exists():
            not_found_message += " Device not found in Eudamed data."

        fda_results = fda_results.distinct()
        eudamed_results = eudamed_results.distinct()
        print(fda_results)
    context = {
        "query": query,
        "fda_results": fda_results,
        "eudamed_results": eudamed_results,
        "not_found_message": not_found_message,
    }
    return render(request, "search_app/search.html", context)


@api_view(["GET"])
def api_search_device(request):
    query = request.GET.get("device_name", "")
    if not query:
        return Response(
            {"error": "Please provide a device_name parameter"}, status=400
        )

    fda_results = FDAData.objects.get_distinct_device_names().filter(
        device_name__iexact=query
    )
    eudamed_results = EudamedData.objects.get_distinct_device_names().filter(
        device_name__iexact=query
    )

    if not fda_results and not eudamed_results:
        return Response({"message": "Device not found in both tables"})
    fda_data = list(fda_results.values())  # Con queryset to list of dic
    eudamed_data = list(
        eudamed_results.values()
    )  # Convert queryset to list of dictionaries

    return Response(
        {
            "fda_data": fda_data,
            "eudamed_data": eudamed_data,
        }
    )
