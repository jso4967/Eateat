from django.shortcuts import render
from django.views.generic import (CreateView, ListView, DetailView, DeleteView, TemplateView,UpdateView,)
from . import models
from . import forms
from django.urls import (reverse, reverse_lazy)
from django.utils import timezone
from datetime import timedelta
import random
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'
    model = models.Meal
    recommended_meal = models.Meal.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["recommended_meal"] = models.Meal.objects.order_by('?').first()
        #TODO : 추천 기준 추가 (날짜, gps, etc)
        current_time = timezone.now()
        object_list = models.Meal.objects.filter(created_date__lte=(current_time - timedelta(days=-3)))
        context["recommended_meal"] = random.choice(object_list)
        return context

class MealCreateView(CreateView):
    model = models.Meal
    form_class = forms.MealForm

    def form_valid(self, form):
        form.save()
        return super(MealCreateView, self).form_valid(form)

    def get_absolute_url(self):
        return reverse('index')

class MealListView(ListView):
    context_object_name = 'Meal_list'
    model = models.Meal

    def get_queryset(self):
        try:
            meal_name = self.request.GET.get('q')
        except:
            meal_name = ''

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


