from django.db import models

class EudamedData(models.Model):
    id = models.AutoField(primary_key=True)
    basic_udi = models.TextField(blank=True, null=True)
    primary_di = models.TextField(blank=True, null=True)
    uuid = models.TextField(blank=True, null=True)
    ulid = models.TextField(blank=True, null=True)
    basic_udi_di_data_ulid = models.TextField(blank=True, null=True)
    risk_class = models.TextField(blank=True, null=True)
    device_name = models.TextField(blank=True, null=True)
    manufacturer_name = models.TextField(blank=True, null=True)
    manufacturer_srn = models.TextField(blank=True, null=True)
    device_status_type = models.TextField(blank=True, null=True)
    manufacturer_status = models.TextField(blank=True, null=True)
    latest_version = models.IntegerField(blank=True, null=True)
    version_number = models.IntegerField(blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    basic_udi_data_version_number = models.IntegerField(blank=True, null=True)
    container_package_count = models.IntegerField(blank=True, null=True)
    authorised_representative_srn = models.TextField(blank=True, null=True)
    authorised_representative_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eudamed_data'

class FdaData(models.Model):
    id = models.AutoField(primary_key=True)
    k_number = models.TextField(blank=True, null=True)
    manufacturer_name = models.TextField(blank=True, null=True)
    contact = models.TextField(blank=True, null=True)
    address1 = models.TextField(blank=True, null=True)
    address2 = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    country_code = models.TextField(blank=True, null=True)
    zip_code = models.TextField(blank=True, null=True)
    postal_code = models.TextField(blank=True, null=True)
    date_received = models.TextField(blank=True, null=True)
    decision_date = models.TextField(blank=True, null=True)
    decision_description = models.TextField(blank=True, null=True)
    product_code = models.TextField(blank=True, null=True)
    statement_or_summary = models.TextField(blank=True, null=True)
    clearance_type = models.TextField(blank=True, null=True)
    third_party_flag = models.TextField(blank=True, null=True)
    expedited_review_flag = models.TextField(blank=True, null=True)
    device_name = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    device_description = models.TextField(blank=True, null=True)
    medical_specialty_description = models.TextField(blank=True, null=True)
    device_class = models.TextField(blank=True, null=True)
    regulation_number = models.TextField(blank=True, null=True)
    submission_type_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fda_data'
