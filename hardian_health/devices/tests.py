from django.test import TestCase
from .models import FdaData, EudamedData
from django.urls import reverse
from django.http import JsonResponse

class SearchFunctionalityTests(TestCase):
    
    def setUp(self):
        """
        Set up initial test data.
        """
        FdaData.objects.create(device_name="TestDevice1", manufacturer_name="ManufacturerA")
        EudamedData.objects.create(device_name="testdevice1", manufacturer_name="ManufacturerA")
        FdaData.objects.create(device_name="TestDevice2", manufacturer_name="ManufacturerB")
    
    def test_device_in_both_tables(self):
        """
        Test that the device found in both tables returns correct data.
        """
        response = self.client.get('/search/', {'device_name': 'TestDevice1'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('ManufacturerA', response.content.decode())

    def test_device_in_fda_only(self):
        """
        Test that a device found only in the FDA table returns correct data.
        """
        response = self.client.get('/search/', {'device_name': 'TestDevice2'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('ManufacturerB', response.content.decode())
        self.assertIn('Not found in Eudamed', response.content.decode())

    def test_device_not_found(self):
        """
        Test that searching for a non-existing device returns a not found message.
        """
        response = self.client.get('/search/', {'device_name': 'NonExistentDevice'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Not found in both tables', response.content.decode())

    def test_case_insensitive_search(self):
        """
        Test that the search is case-insensitive.
        """
        response = self.client.get('/search/', {'device_name': 'testdevice1'})  # Lowercase search query
        self.assertEqual(response.status_code, 200)
        self.assertIn('ManufacturerA', response.content.decode())

    def test_api_search_device(self):
        """
        Test API endpoint for returning device search results in JSON format.
        """
        response = self.client.get(reverse('api_search'), {'device_name': 'TestDevice1'})
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertIn('fda_data', json_response)
        self.assertIn('eudamed_data', json_response)
        self.assertEqual(json_response['fda_data'][0]['manufacturer_name'], 'ManufacturerA')
        self.assertEqual(json_response['eudamed_data'][0]['manufacturer_name'], 'ManufacturerA')

    def test_api_device_not_found(self):
        """
        Test API endpoint for a non-existing device in both tables.
        """
        response = self.client.get(reverse('api_search'), {'device_name': 'NonExistentDevice'})
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertEqual(json_response['fda_data'], [])
        self.assertEqual(json_response['eudamed_data'], [])