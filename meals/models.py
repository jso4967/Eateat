from django.db import models

# Create your models here.
class Meal(models.Model):
    meal_name = models.CharField(max_length=200, default='default')
    restaurant_name = models.CharField(max_length=200, default='default')
    # price_range =
    # satisfaction =
    # visit_frequency =
    # location =

    def __str__(self):
        return self.meal_name