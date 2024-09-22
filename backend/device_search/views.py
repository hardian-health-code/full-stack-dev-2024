from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FdaData, EudamedData

class DeviceSearchView(APIView):
    """
    Unified search view that returns devices from both fda_data and eudamed_data.
    If no device_name is provided, it returns all devices. If a partial query is provided,
    it returns all devices that start with that query.
    """
    def get(self, request, *args, **kwargs):
        device_name = request.query_params.get('device_name', '').strip().lower()

        # Initialize variables
        combined_results = []
        in_both_datasets = False

        if device_name:
            # Perform case-insensitive "startswith" search in both tables if device_name is provided
            fda_data = FdaData.objects.filter(device_name__istartswith=device_name)
            eudamed_data = EudamedData.objects.filter(device_name__istartswith=device_name)

            # Process FDA data
            if fda_data.exists():
                for device in fda_data:
                    combined_results.append({
                    'device_name': device.device_name,
                    'manufacturer_name': device.manufacturer_name,
                    'k_number': device.k_number,
                    'contact': device.contact,
                    'address1': device.address1,
                    'address2': device.address2,
                    'city': device.city,
                    'state': device.state,
                    'country_code': device.country_code,
                    'zip_code': device.zip_code,
                    'postal_code': device.postal_code,
                    'date_received': device.date_received,
                    'decision_date': device.decision_date,
                    'decision_description': device.decision_description,
                    'product_code': device.product_code,
                    'statement_or_summary': device.statement_or_summary,
                    'clearance_type': device.clearance_type,
                    'third_party_flag': device.third_party_flag,
                    'expedited_review_flag': device.expedited_review_flag,
                    'device_description': device.device_description,
                    'medical_specialty_description': device.medical_specialty_description,
                    'device_class': device.device_class,
                    'regulation_number': device.regulation_number,
                    'submission_type_id': device.submission_type_id,
                    'source': 'FDA'
                    })

            # Process EUDAMED data
            if eudamed_data.exists():
                for device in eudamed_data:
                    combined_results.append({
                    'device_name': device.device_name,
                    'manufacturer_name': device.manufacturer_name,
                    'basic_udi': device.basic_udi,
                    'primary_di': device.primary_di,
                    'uuid': device.uuid,
                    'ulid': device.ulid,
                    'basic_udi_di_data_ulid': device.basic_udi_di_data_ulid,
                    'risk_class': device.risk_class,
                    'manufacturer_srn': device.manufacturer_srn,
                    'device_status_type': device.device_status_type,
                    'manufacturer_status': device.manufacturer_status,
                    'latest_version': device.latest_version,
                    'version_number': device.version_number,
                    'reference': device.reference,
                    'basic_udi_data_version_number': device.basic_udi_data_version_number,
                    'container_package_count': device.container_package_count,
                    'authorised_representative_srn': device.authorised_representative_srn,
                    'authorised_representative_name': device.authorised_representative_name,
                    'source': 'EUDAMED'
                    })

            # Check if the device is present in both datasets
            if fda_data.exists() and eudamed_data.exists():
                in_both_datasets = True

        else:
            # No device_name provided, return all devices from both tables
            fda_data = FdaData.objects.all()
            eudamed_data = EudamedData.objects.all()

            # Process all FDA data
            for device in fda_data:
                combined_results.append({
                    'device_name': device.device_name,
                    'manufacturer_name': device.manufacturer_name,
                    'k_number': device.k_number,
                    'contact': device.contact,
                    'address1': device.address1,
                    'address2': device.address2,
                    'city': device.city,
                    'state': device.state,
                    'country_code': device.country_code,
                    'zip_code': device.zip_code,
                    'postal_code': device.postal_code,
                    'date_received': device.date_received,
                    'decision_date': device.decision_date,
                    'decision_description': device.decision_description,
                    'product_code': device.product_code,
                    'statement_or_summary': device.statement_or_summary,
                    'clearance_type': device.clearance_type,
                    'third_party_flag': device.third_party_flag,
                    'expedited_review_flag': device.expedited_review_flag,
                    'device_description': device.device_description,
                    'medical_specialty_description': device.medical_specialty_description,
                    'device_class': device.device_class,
                    'regulation_number': device.regulation_number,
                    'submission_type_id': device.submission_type_id,
                    'source': 'FDA'
                })

            # Process all EUDAMED data
            for device in eudamed_data:
                combined_results.append({
                    'device_name': device.device_name,
                    'manufacturer_name': device.manufacturer_name,
                    'basic_udi': device.basic_udi,
                    'primary_di': device.primary_di,
                    'uuid': device.uuid,
                    'ulid': device.ulid,
                    'basic_udi_di_data_ulid': device.basic_udi_di_data_ulid,
                    'risk_class': device.risk_class,
                    'manufacturer_srn': device.manufacturer_srn,
                    'device_status_type': device.device_status_type,
                    'manufacturer_status': device.manufacturer_status,
                    'latest_version': device.latest_version,
                    'version_number': device.version_number,
                    'reference': device.reference,
                    'basic_udi_data_version_number': device.basic_udi_data_version_number,
                    'container_package_count': device.container_package_count,
                    'authorised_representative_srn': device.authorised_representative_srn,
                    'authorised_representative_name': device.authorised_representative_name,
                    'source': 'EUDAMED'
                })

        # Return combined results with a flag for in_both_datasets if applicable
        return Response({
            'results': combined_results,
            'in_both_datasets': in_both_datasets
        })
