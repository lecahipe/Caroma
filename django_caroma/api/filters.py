import django_filters
from data.models import Restaurant

class RestaurantFilter(django_filters.FilterSet):
    postal_codes = django_filters.CharFilter(method='filter_postal_codes', label='Postal Codes')
    min_rating = django_filters.NumberFilter(field_name='rating__avg', lookup_expr='gte', label='Minimum Rating')
    max_rating = django_filters.NumberFilter(field_name='rating__avg', lookup_expr='lte', label='Maximum Rating')
    exclude_types = django_filters.CharFilter(method='filter_exclude_types', label='Exclude Restaurant Type')
   
    class Meta:
        model = Restaurant
        fields = ['postal_code', 'min_rating', 'max_rating']

    def filter_postal_codes(self, queryset, name, value):
        postal_codes_list = value.split(',')
        return queryset.filter(postal_code__in=postal_codes_list)
    
    def exclude_types(self, queryset, name, value):
        exclude_types_list = value.split(',')
        return queryset.exclude(restaurant_type__in=exclude_types_list)
    
    
