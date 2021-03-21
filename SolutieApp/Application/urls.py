from django.urls import path, include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.all_products, name = 'all_products'),
]