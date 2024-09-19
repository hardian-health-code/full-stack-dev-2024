from django.db import models

class FdaData(models.Model):
    device_name = models.CharField(max_length=255)
    manufacturer_name = models.CharField(max_length=255)

class EudamedData(models.Model):
    device_name = models.CharField(max_length=255)
    manufacturer_name = models.CharField(max_length=255)
