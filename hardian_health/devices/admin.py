from django.contrib import admin
from .models import FdaData, EudamedData

@admin.register(FdaData)
class FdaDataAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'manufacturer_name')

@admin.register(EudamedData)
class EudamedDataAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'manufacturer_name')
