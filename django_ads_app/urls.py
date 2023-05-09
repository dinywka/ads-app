from django.contrib import admin
from django.urls import path
from django_ads_app import views


urlpatterns = [
    path('', views.home),
    path('json/', views.get_json),
    path('login/', views.login),
]