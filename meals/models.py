from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Meal(models.Model):
    CHOICES = [('높음', '높음'),
               ('중간', '중간'),
               ('낮음', '낮음')]

    meal_photo = models.ImageField(blank=True)
    meal_name = models.CharField(max_length=200, default='')
    restaurant_name = models.CharField(max_length=200, default='')
    price_range = models.CharField(max_length=2, choices=CHOICES, default="")
    satisfaction = models.CharField(max_length=2, choices=CHOICES, default="")
    created_date = models.DateTimeField(default=timezone.now)
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> parent of 246b13b... TEST AT 8:19

>>>>>>> parent of 246b13b... TEST AT 8:19
    def get_absolute_url(self):  # redirect시 활용
        return reverse('index')

    def __str__(self):
        return self.meal_name