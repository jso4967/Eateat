from django.shortcuts import render
from django.views.generic import (CreateView, ListView, DetailView, DeleteView)

# Create your views here.

class UploadMeal(CreateView):
    pass

class MealList(ListView):
    pass

class MealDetail(DetailView):
    pass

class DeleteMeal(DeleteView):
    pass