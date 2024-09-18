#Below is an example of a test case that tests the search functionality of the application. You can modify any of the existing test code or add new test cases as needed.

from django.test import TestCase
from django.urls import reverse
from devices.models import FDAData, EudamedData

class SearchFunctionalityTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Create sample data for testing
        FDAData.objects.create(device_name='Device1', k_number='123', manufacturer_name='Manufacturer1')
        EudamedData.objects.create(device_name='Device1', basic_udi='UDI123', manufacturer_name='Manufacturer1')
        FDAData.objects.create(device_name='Device2', k_number='456', manufacturer_name='Manufacturer2')
        EudamedData.objects.create(device_name='Device3', basic_udi='UDI456', manufacturer_name='Manufacturer3')

    def test_search_device_in_both_tables(self):
        response = self.client.get(reverse('search_view'), {'device_name': 'Device1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'device1')
        self.assertNotContains(response, 'No FDA Devices Found')
        self.assertNotContains(response, 'No Eudamed Devices Found')

    def test_search_device_in_one_table(self):
        response = self.client.get(reverse('search_view'), {'device_name': 'Device2'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'device2')
        self.assertContains(response, 'No Eudamed Devices Found')

    def test_search_device_not_found(self):
        response = self.client.get(reverse('search_view'), {'device_name': 'NonExistentDevice'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Not found')

    def test_api_search_device_in_both_tables(self):
        response = self.client.get(reverse('api_search_view'), {'device_name': 'Device1'})
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertIn('fda_devices', response_json)
        self.assertIn('eudamed_devices', response_json)
        self.assertEqual(len(response_json['fda_devices']), 1)
        self.assertEqual(len(response_json['eudamed_devices']), 1)

    def test_api_search_device_in_one_table(self):
        response = self.client.get(reverse('api_search_view'), {'device_name': 'Device2'})
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertIn('fda_devices', response_json)
        self.assertIn('eudamed_devices', response_json)
        self.assertEqual(len(response_json['fda_devices']), 1)
        self.assertEqual(len(response_json['eudamed_devices']), 0)

    def test_api_search_device_not_found(self):
        response = self.client.get(reverse('api_search_view'), {'device_name': 'NonExistentDevice'})
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertIn('fda_devices', response_json)
        self.assertIn('eudamed_devices', response_json)
        self.assertEqual(len(response_json['fda_devices']), 0)
        self.assertEqual(len(response_json['eudamed_devices']), 0)
