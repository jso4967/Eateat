from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

# class Restaurant(models.Model):
#     restaurant_name = models.CharField(max_length=200, default='')
#     gps_x = models.FloatField(default=0.0)
#     gps_y = models.FloatField(default=0.0)
#
#     def get_absolute_url(self):
#         return reverse('index')
#
#     def __str__(self):
#         return self.restaurant_name


class Meal(models.Model):
    CHOICES = [('높음', '높음'),
               ('중간', '중간'),
               ('낮음', '낮음')]

    meal_photo = models.ImageField(blank=True)
    meal_name = models.CharField(max_length=200, default='', unique=True)
    restaurant_name = models.CharField(max_length=200, default='')
    price_range = models.CharField(max_length=2, choices=CHOICES, default="")
    satisfaction = models.CharField(max_length=2, choices=CHOICES, default="")
    recent_visit_date = models.DateTimeField(default=timezone.now)
    count = models.IntegerField(default=0)

    def get_absolute_url(self):  # redirect시 활용
        return reverse('index')

    def __str__(self):
        return self.meal_name



