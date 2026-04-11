from django.urls import path
from . import views
from .views import registratciya, log_out

urlpatterns = [
    path('', views.home, name='home'),
    path('clothes/<int:pk>/', views.clothes_detail, name='clothes_detail'),
    path('reg/', registratciya, name='Registration'),
    path('logout/', log_out, name='logout'),
]