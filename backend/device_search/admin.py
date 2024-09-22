from django.contrib import admin
from .models import FdaData, EudamedData

@admin.register(FdaData)
class FDADataAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'manufacturer_name')  

@admin.register(EudamedData)
class EUDAMEDDataAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'manufacturer_name')  
