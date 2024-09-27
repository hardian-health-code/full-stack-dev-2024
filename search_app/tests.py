from django.db import connection
from django.test import TestCase

from search_app.models import EudamedData, FDAData


class SearchFunctionalityTests(TestCase):

    def setUp(self):
        """
        Set up initial test data.
        """
        # Create the fda_data table manually
        with connection.cursor() as cursor:
            cursor.execute(
                """
                        CREATE TABLE IF NOT EXISTS fda_data (
                            device_name VARCHAR(255) PRIMARY KEY,
                            manufacturer_name VARCHAR(255)
                        );
                    """
            )
            cursor.execute(
                """
                        CREATE TABLE IF NOT EXISTS eudamed_data (
                            device_name VARCHAR(255) PRIMARY KEY,
                            manufacturer_name VARCHAR(255)
                        );
                    """
            )

        FDAData.objects.create(
            device_name="TestDevice1", manufacturer_name="ManufacturerA"
        )
        FDAData.objects.create(
            device_name="testdevice1", manufacturer_name="ManufacturerB"
        )
        EudamedData.objects.create(
            device_name="TestDevice1", manufacturer_name="ManufacturerA"
        )
        FDAData.objects.create(
            device_name="TestDevice2", manufacturer_name="ManufacturerB"
        )
        EudamedData.objects.create(
            device_name="TestDevice2", manufacturer_name="ManufacturerB"
        )
        EudamedData.objects.create(
            device_name="testdevice2", manufacturer_name="ManufacturerD"
        )

    def test_device_in_both_tables(self):
        """
        Test that the device found in both tables returns correct data.
        """
        # Perform the search operation
        response = self.client.get(
            "/v1/device/", {"device_name": "TestDevice1"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("ManufacturerA", response.content.decode())

    def test_device_in_fda_only(self):
        """
        Test that a device found only in the FDA table returns correct data.
        """
        response = self.client.get(
            "/v1/device/", {"device_name": "TestDevice2"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("ManufacturerB", response.content.decode())

    def test_device_not_found(self):
        """
        Test that searching for a non-existing
        device returns a not found message.
        """
        response = self.client.get(
            "/v1/device/", {"device_name": "NonExistentDevice"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Device not found in both tables", response.content.decode()
        )

    def test_invalid_query(self):
        # Test with an empty query parameter
        response = self.client.get("/v1/device/", {"device_name": ""})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data["error"], "Please provide a device_name parameter"
        )
