from django.shortcuts import render
from django.views.generic import (CreateView, ListView, DetailView, DeleteView, TemplateView,UpdateView,)
from . import models
from django.urls import (reverse, reverse_lazy)
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

    def get_absolute_url(self):
        return reverse('index')

class MealListView(ListView):
    context_object_name = 'Meal_list'
    model = models.Meal

    def get_queryset(self):
        try:
            meal_name = self.request.GET.get('q')
            print('test1')
        except:
            meal_name = ''
            print('test2')

        if meal_name != ('' or None):
            object_list = models.Meal.objects.filter(meal_name__icontains = meal_name)
            print(meal_name, object_list)
        else:
            object_list = models.Meal.objects.all()
        return object_list

class MealDetail(DetailView):
    model = models.Meal
    context_object_name = 'Meal_detail'
    # template_name = 'meal_detail.html'


class MealDelete(DeleteView):
    model = models.Meal
    success_url = reverse_lazy('meals:list')
    context_object_name = 'Meal_delete'

class MealUpdateView(UpdateView):
    fields = ("meal_photo", "meal_name", "restaurant_name", "price_range", "satisfaction")
    model = models.Meal


