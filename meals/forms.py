from django import forms
from . import models

class MealForm(forms.ModelForm):

    class Meta:
        model = models.Meal
        fields = ('meal_name','meal_photo','restaurant_name','price_range','satisfaction',)

        widgets = {
            'meal_name' : forms.TextInput(attrs={'class':'form-control'}),
            'restaurant_name' : forms.TextInput(attrs={'class':'form-control'}),
            'price_range' : forms.TextInput(attrs={'class':'form-control'}),
            'satisfaction' : forms.TextInput(attrs={'class':'form-control'}),

        }