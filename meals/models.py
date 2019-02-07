from django.db import models

# Create your models here.
class Meal(models.Model):
    meal_name = models.CharField(max_length=200)
    restaurant_name = models.CharField(max_length=200)
    # price_range =
    # satisfaction =
    # visit_frequency =
    # location =

    def __str__(self):
        pass