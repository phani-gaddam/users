from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('push',views.home),
    path('view',views.viewall),
]