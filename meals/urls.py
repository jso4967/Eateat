from django.urls import path
from . import views


app_name = 'meals'

urlpatterns = [
    path('create/', views.MealCreateView.as_view(), name='create'),
    path('list/ ', views.MealListView.as_view(), name ='list' ),
    path('detail/<int:pk>', views.MealDetail.as_view(), name = 'detail'),
    path('detail/<int:pk>/delete/', views.MealDelete.as_view(), name = 'delete'),

]
