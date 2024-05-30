# insert_data.py

import json
from django.core.management.base import BaseCommand
from data.models import Restaurant, MenuCard, Rating, Service, Property, ReviewTag, Utilization, OpeningTime
class Command(BaseCommand):
    help = 'Insert data from JSON file into the default database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        
        # Open and load JSON data
        with open(json_file, 'r') as file:
            restaurants_data = json.load(file)

        for data in restaurants_data:
            # Create restaurant
            restaurant = Restaurant.objects.create(
                name = data['name'],
                place_id =data['place_id'],
                street = data['street'],
                postal_code = data['postal_code'],
                city = data['city'],
                state = data['state'],
                country = data['country'],
                phone = data['phone'],  
                place_url = data['place_url'],
                website_url = data['website_url'],
                type = data['type'],
                opening_time_monday = data['opening_time_monday'],
                opening_time_tuesday = data['opening_time_monday'],
                opening_time_wednesday = data['opening_time_monday'],
                opening_time_thursday = data['opening_time_monday'],
                opening_time_friday = data['opening_time_monday'],
                opening_time_saturday = data['opening_time_monday'],
                opening_time_sunday = data['opening_time_monday'],
                longitude = data['longitude'],
                latitude = data['latitude']
            )
            # Insert services
            for service_data in data['services']:
                Service.objects.create(restaurant=restaurant, url=service_data['url'])
            
            for properties_data in data['properties']:
                Property.objects.create(restaurant=restaurant, value=properties_data)
                
            ReviewTag.objects.create(restaurant=restaurant, tags=data['review_tags'])
                
            # Insert menu cards
            for menu_card_data in data['menu_cards']:
                menu_card = MenuCard.objects.create(restaurant=restaurant, type=menu_card_data['type'])
                for item_data in menu_card_data['items']:
                    item =  menu_card.items.create(
                        name=item_data['name'],
                        description=item_data['description'],
                        price=item_data['price']
                    )
                    if len(item_data.get('ingredients')) >0:
                        for ingredient in item_data['ingredients']:
                            item.ingredients.create(name=ingredient)
            
            utilization_keys = [key.split('_')[1] for key in data if key.startswith('utilization_')]

            for key_day in utilization_keys:
                for utilization_data in data['utilization_'+key_day]:
                    Utilization.objects.create(
                        restaurant=restaurant,
                        day_of_week=key_day,
                        hour=utilization_data['hour'],
                        occupancy_percent=utilization_data['occupancyPercent']
                    )
            
            opening_times_key = [key for key in data if key.startswith('opening_time_')]            
            for o_key in opening_times_key:
                day_of_week = o_key.split('opening_time_')[1]
                OpeningTime.objects.create(
                    restaurant=restaurant,
                    day_of_week=day_of_week,
                    time=data['opening_time_'+day_of_week]
                )
                
                
            # Insert ratings
            for rating_data in data['ratings']:
                Rating.objects.create(
                    restaurant=restaurant,
                    source=rating_data['source'],
                    avg=rating_data['avg'],
                    one_star_count=rating_data['one_star_count'],
                    two_star_count=rating_data['two_star_count'],
                    three_star_count=rating_data['three_star_count'],
                    four_star_count=rating_data['four_star_count'],
                    five_star_count=rating_data['five_star_count'],
                    total_count=rating_data['total_count']
                )

        self.stdout.write(self.style.SUCCESS('Data inserted successfully'))
