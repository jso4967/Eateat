from django.urls import path
from . import views


app_name = 'meals'

urlpatterns = [
    path('create/', views.MealCreateView.as_view(), name='create'),
    path('list/ ', views.MealListView.as_view(), name ='list' ),
    path('detail/', views.MealDetail.as_view(), name = 'detail')
#
]
