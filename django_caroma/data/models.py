from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    place_id = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    place_url = models.URLField()
    website_url = models.URLField()
    type = models.CharField(max_length=100)
    opening_time_monday = models.CharField(max_length=25)
    opening_time_tuesday = models.CharField(max_length=25)
    opening_time_wednesday = models.CharField(max_length=25)
    opening_time_thursday = models.CharField(max_length=25)
    opening_time_friday = models.CharField(max_length=25)
    opening_time_saturday = models.CharField(max_length=25)
    opening_time_sunday = models.CharField(max_length=25)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    
    class Meta:
        indexes = [
            models.Index(fields=['type']),
            models.Index(fields=['longitude', 'latitude']),
            models.Index(fields=['postal_code']),
        ]
    
    def __str__(self):
        return f"{self.name}"

class MenuCard(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_cards')
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.restaurant} - {self.name}"
    
    
class MenuItem(models.Model):
    menu_card = models.ForeignKey(MenuCard, on_delete=models.CASCADE, related_name='items')
    model = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100, blank=True, null=True)
    price_raw = models.FloatField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.menu_card} - {self.name}"


class MenuItemIngredient(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.menu_item} - {self.name}"

class Rating(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='ratings')
    source = models.CharField(max_length=100)
    avg = models.FloatField()
    one_star_count = models.IntegerField()
    two_star_count = models.IntegerField()
    three_star_count = models.IntegerField()
    four_star_count = models.IntegerField()
    five_star_count = models.IntegerField()
    total_count = models.IntegerField()
    
    def __str__(self):
        return f"{self.restaurant} - {self.avg}"

class Utilization(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='utilizations')
    day_of_week = models.CharField(max_length=10)
    hour = models.IntegerField()
    occupancy_percent = models.FloatField()
    
    def __str__(self):
        return f"{self.restaurant} - {self.day_of_week} - {self.occupancy_percent}"
    
class OpeningTime(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='opening_times')
    day_of_week = models.CharField(max_length=10)
    time = models.CharField(max_length=25)
    
    def __str__(self):
        return f"{self.restaurant} - {self.day_of_week} - {self.time}"
    
class Property(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='properties')
    key = models.CharField(max_length=100, blank=True, null=True)
    value = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.restaurant} - {self.value}"

class ReviewTag(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='review_tags')
    tags = models.TextField()
    
    def __str__(self):
        return f"{self.restaurant} - {self.tags}"


class Service(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='services')
    url = models.URLField()
    
    def __str__(self):
        return f"{self.restaurant} - {self.url}"