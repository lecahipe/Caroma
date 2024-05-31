import pytest
from rest_framework.test import APIClient
from api.factories import RestaurantFactory
from django.urls import reverse

from data.models import Restaurant
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_caroma.settings')

@pytest.mark.django_db
class TestRestaurantView:
    '''
        Test the UserDeviceMetabolicDataView view
    '''
    def setup_method(self):
        self.client = APIClient()
        self.url = reverse('restaurant-list')
        self.data_count = 4
        self.page_size = 4
        self.data = RestaurantFactory.create_batch(self.data_count)

    def test_list_view(self):
        '''
            Test that the view can list all records
        '''
        response = self.client.get(self.url)
        assert response.status_code == 200 # tests that the response status code is 200
        assert len(response.json()) == self.data_count # tests that the number of records returned is equal to the number of records created
        assert len(response.data['results']) == self.page_size # tests that the page size is 5
        assert 'next' in response.data # tests that there is a next page in the response
        assert response.data['previous'] is None # tests that there is no previous page in the response

    