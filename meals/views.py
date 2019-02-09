from django.shortcuts import render
from django.views.generic import (CreateView, ListView, DetailView, DeleteView, TemplateView)
from . import models
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class MealCreateView(CreateView):
    fields = ("meal_name", "restaurant_name")
    model = models.Meal

class MealList(ListView):
    pass

class MealDetail(DetailView):
    pass

class DeleteMeal(DeleteView):
    pass