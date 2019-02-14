from django.shortcuts import render
from django.views.generic import (CreateView, ListView, DetailView, DeleteView, TemplateView)
from . import models
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'
    model = models.Meal
    recommended_meal = models.Meal.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recommended_meal"] = models.Meal.objects.order_by('?').first()
        return context

class MealCreateView(CreateView):
    fields = ("meal_photo", "meal_name", "restaurant_name", "price_range", "satisfaction")
    model = models.Meal

class MealListView(ListView):
    pass

class MealDetail(DetailView):
    pass

class DeleteMeal(DeleteView):
    pass

def base_layout(request):
    template = 'base.html'
    return render(request, template)