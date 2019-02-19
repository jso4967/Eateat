from django import forms
from . import models


class MealForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(MealForm, self).__init__(*args, **kwargs)
    #     self.fields['meal_name'] = forms.ModelChoiceField(queryset=models.Meal.objects.values_list('meal_name', flat=True))
    #     self.fields['restaurant_name'] = forms.ModelChoiceField(queryset=models.Meal.objects.values_list('restaurant_name', flat=True))
    class Meta:

        model = models.Meal
        fields = ('meal_name','meal_photo','restaurant_name','price_range','satisfaction', 'recent_visit_date', 'count')
        price_range = forms.ChoiceField(choices=[('높음', '높음'), ('중간', '중간'), ('낮음', '낮음')]),
        satisfaction = forms.ChoiceField(choices=[('높음', '높음'), ('중간', '중간'), ('낮음', '낮음')]),
        count = forms.IntegerField(disabled=True)
        widgets = {

            'meal_name' : forms.TextInput(attrs={'class':'form-control'}),
        }

        def save(self, commit=True):
            self.instance = models.Meal(**self.cleaned_data)
            if commit:
                self.instance.save()

            return self.instance

# class MealUpdateForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(MealForm, self).__init__(*args, **kwargs)
#         self.fields['meal_name'] = forms.ModelChoiceField(queryset=models.Meal.objects.values('meal_name'))
#         self.fields['restaurant_name'] = forms.ModelChoiceField(queryset=models.Meal.objects.values('restaurant_name'))