from django import forms
from . import models

class MealForm(forms.ModelForm):

    class Meta:
        model = models.Meal
        fields = ('meal_name','meal_photo','restaurant_name','price_range','satisfaction',)
        price_range = forms.ChoiceField(choices=[('높음', '높음'), ('중간', '중간'), ('낮음', '낮음')]),
        satisfaction = forms.ChoiceField(choices=[('높음', '높음'), ('중간', '중간'), ('낮음', '낮음')]),
        widgets = {

            'meal_name' : forms.TextInput(attrs={'class':'form-control'}),
            'restaurant_name' : forms.TextInput(attrs={'class':'form-control'}),

        }