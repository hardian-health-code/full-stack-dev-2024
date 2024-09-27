from django.db import models
from django.db.models.functions import Lower

# Create your models here.


class FDADataManager(models.Manager):
    def get_distinct_device_names(self):
        return (
            self.annotate(lower_device_name=Lower("device_name"))
            .values("lower_device_name")
            .distinct()
        )


class EudamedData(models.Manager):
    def get_distinct_device_names(self):
        return (
            self.annotate(lower_device_name=Lower("device_name"))
            .values("lower_device_name")
            .distinct()
        )


class FDAData(models.Model):
    device_name = models.CharField(max_length=255, primary_key=True)
    manufacturer_name = models.CharField(max_length=255, null=True, blank=True)
    # Add other fields from fda_data table
    objects = FDADataManager()

    class Meta:
        db_table = "fda_data"  # Ensure this matches the table name
        managed = False  # Inform Django not to manage this table


class EudamedData(models.Model):
    device_name = models.CharField(max_length=255, primary_key=True)
    manufacturer_name = models.CharField(max_length=255, null=True, blank=True)
    # Add other fields from eudamed_data table
    objects = EudamedData()

    class Meta:
        db_table = "eudamed_data"  # Ensure this matches the table name
        managed = False  # Inform Django not to manage this table
