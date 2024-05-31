import pytest
from rest_framework.test import APIClient
from api.factories import RestaurantFactory
from django.urls import reverse

from data.models import Restaurant
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_caroma.settings')

from django.core.management import call_command

@pytest.fixture(autouse=True)
def clean_db():
    call_command('flush', '--noinput')


@pytest.mark.django_db
class TestRestaurantView:
    '''
        Test the UserDeviceMetabolicDataView view
    '''
    def setup_method(self, clean_db):
        self.client = APIClient()
        self.url = reverse('restaurant-list')
        self.data_count = 4
        self.page_size = 4
        self.data = RestaurantFactory.create_batch(self.data_count)

    def test_list_view(self):
        '''
            Test that the view can list all restaurant records
        '''
        response = self.client.get(self.url)
        print(response.data)
        assert response.status_code == 200 # tests that the response status code is 200
        assert len(response.json()) == self.data_count # tests that the number of records returned is equal to the number of records created
        assert len(response.data['results']) == self.page_size # tests that the page size is 5
        assert 'next' in response.data # tests that there is a next page in the response
        assert response.data['previous'] is None # tests that there is no previous page in the response

    def test_list_view_filter_postal_codes(self):
        '''
            Test that the view can list filter records by postal_code or postal_codes      
        '''
        postal_code_1 = self.data[0].postal_code
        postal_code_2 = self.data[1].postal_code
        postal_code_str = f"{postal_code_1},{postal_code_2}"
        response = self.client.get(self.url, {'postal_codes': postal_code_str})
        assert response.status_code == 200 # tests that the response status code is 200
        data = response.json()
        result_1 = data['results'][0]
        assert result_1['postal_code'] == postal_code_1 or postal_code_2
        
    
    def test_list_view_filter_postal_codes_exclude_type(self):
        '''
            Test that the view can list filter records by postal_code or postal_codes but exclude by type
        '''
        data = self.data
        postal_code_1 = data[0].postal_code
        postal_code_2 = data[1].postal_code
        type_1 = data[0].type
        type_2 = data[1].type
        assert type_1 != type_2
        postal_code_str = f"{postal_code_1},{postal_code_2}"
        response = self.client.get(self.url, {'postal_codes': postal_code_str, 'exclude_types':type_1})
        assert response.status_code == 200 # tests that the response status code is 200
        data = response.json()
        result_1 = data['results'][0]
        assert result_1['type'] == type_2
    
    