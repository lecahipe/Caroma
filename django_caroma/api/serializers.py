from rest_framework import serializers
from data.models import Restaurant, MenuCard, MenuItem, MenuItemIngredient, Rating, Utilization, Property, ReviewTag
class MenuItemIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItemIngredient
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):
    ingredients = MenuItemIngredientSerializer(many=True, read_only=True)
    class Meta:
        model = MenuItem
        fields = '__all__'


class MenuCardSerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True, read_only=True)
    class Meta:
        model = MenuCard
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
        
class UtilizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilization
        fields = ['hour', 'occupancy_percent'] 

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['value']


class ReviewTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewTag
        fields = ['tags']
    
class RestaurantSerializer(serializers.ModelSerializer):
    menu_cards = MenuCardSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    properties = PropertySerializer(source='properties.all', many=True)
    review_tags = ReviewTagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Restaurant
        fields = '__all__'
        
    def get_utilization_(self, obj, day_of_week):
        utilizations = obj.utilizations.filter(day_of_week=day_of_week)
        return UtilizationSerializer(utilizations, many=True).data
   
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        for day in days_of_week:
            ret[f'utilization_{day}'] = self.get_utilization_(instance, day)
        return ret