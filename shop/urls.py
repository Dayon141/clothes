from django.urls import path
from . import views

urlpatterns = [
    path('', views.clothes_list, name='clothes_list'),
    path('clothes/<int:pk>/', views.clothes_detail, name='clothes_detail'),
]