import factory
from factory.django import DjangoModelFactory
from data.models import Restaurant

class RestaurantFactory(DjangoModelFactory):
    class Meta:
        model = Restaurant
    name = factory.Faker('company')
    place_id = factory.Faker('word')
    street = factory.Faker('address')
    postal_code = factory.Faker('postcode')
    city = factory.Faker('city')
    state = factory.Faker('state')
    country = factory.Faker('country')
    phone = factory.Faker('phone_number')
    place_url = factory.Faker('url')
    opening_time_monday = factory.Iterator(["10:00 to 21:00", "09:00 to 20:00", "08:00 to 19:00"])
    opening_time_tuesday = factory.Iterator(["10:00 to 21:00", "09:00 to 20:00", "08:00 to 19:00"])
    opening_time_wednesday = factory.Iterator(["10:00 to 21:00", "09:00 to 20:00", "08:00 to 19:00"])
    opening_time_thursday = factory.Iterator(["10:00 to 21:00", "09:00 to 20:00", "08:00 to 19:00"])
    opening_time_friday = factory.Iterator(["10:00 to 21:00", "09:00 to 20:00", "08:00 to 19:00"])
    opening_time_saturday = factory.Iterator(["10:00 to 21:00", "09:00 to 20:00", "08:00 to 19:00"])
    opening_time_sunday = factory.Iterator(["10:00 to 21:00", "09:00 to 20:00", "08:00 to 19:00"])
    longitude = factory.Faker('longitude')
    latitude = factory.Faker('latitude')
    type = factory.Faker('word')


# class MenuCardFactory(DjangoModelFactory):
#     restaurant = factory.SubFactory(RestaurantFactory)
#     name = factory.Faker('name')
#     type = factory.Faker('word')
    
# class MenuItemFactory(DjangoModelFactory):
#     menu_card = factory.SubFactory(MenuCardFactory)
#     model = factory.Faker('word')
#     name = factory.Faker('name')
#     description = factory.Faker('text')
#     price_raw = factory.Faker('pydecimal')
#     price = factory.Faker('pydecimal')
#     type = factory.Faker('word')

# class MenuItemIngredientFactory(DjangoModelFactory):
#     menu_item = factory.SubFactory(MenuItemFactory)
#     name = factory.Faker('name')

# class Rating(DjangoModelFactory):
#     restaurant = factory.SubFactory(RestaurantFactory)
#     source = factory.Faker('word')
#     avg = factory.Faker('random_int', min=0, max=5)
#     one_star_count = factory.Faker('random_int')
#     two_star_count = factory.Faker('random_int')
#     three_star_count = factory.Faker('random_int')
#     four_star_count = factory.Faker('random_int')
#     five_star_count = factory.Faker('random_int')
#     total_count = factory.Faker('random_int')

# class UtilizationFactory(DjangoModelFactory):
#     restaurant = factory.SubFactory(RestaurantFactory)
#     day_of_week = factory.Faker('day_of_week')
#     hour = factory.Faker('random_int', min=00, max=24)
#     occupancy_percent = factory.Faker('random_int', min=0, max=100)

# class OpeningTimeFactory(DjangoModelFactory):
#     restaurant = factory.SubFactory(RestaurantFactory)
#     day_of_week = factory.Faker('day_of_week')
#     time = factory.Iterator(["10:00 to 21:00", "09:00 to 20:00", "08:00 to 19:00"])
    
# class PropertyFactory(DjangoModelFactory):
#     restaurant = factory.SubFactory(RestaurantFactory)
#     key = factory.Faker('random_int')
#     value = factory.Faker('word')

# class ReviewTagFactory(DjangoModelFactory):
#     restaurant = factory.SubFactory(RestaurantFactory)
#     tags = factory.Faker('tags')

# class ServiceFactory(DjangoModelFactory):
#     restaurant = factory.SubFactory(RestaurantFactory)
#     url = factory.Faker('url')