import django_filters
from data.models import Restaurant
from urllib.parse import unquote

class RestaurantFilter(django_filters.FilterSet):
    postal_codes = django_filters.CharFilter(method='filter_postal_codes', label='Postal Codes')
    exclude_types = django_filters.CharFilter(method='filter_exclude_types', label='Exclude Restaurant Type')
    min_rating = django_filters.NumberFilter(field_name='ratings__avg', lookup_expr='gte', label='Minimum Rating')
    max_rating = django_filters.NumberFilter(field_name='ratings__avg', lookup_expr='lte', label='Maximum Rating')
   
    class Meta:
        model = Restaurant
        fields = ['postal_codes', 'exclude_types', 'min_rating', 'max_rating']

    def filter_postal_codes(self, queryset, name, value):
        ''' method to filter restaurant by postal codes in the queryset'''
        decoded_value = unquote(value)
        postal_codes_list = decoded_value.split(',')
        return queryset.filter(postal_code__in=postal_codes_list)
    
    def filter_exclude_types(self, queryset, name, value):
        ''' method to exclude restaurant types from the queryset'''
        decoded_value = unquote(value)
        exclude_types_list = decoded_value.split(',')
        return queryset.exclude(type__in=exclude_types_list)
    
    
