from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('table/', views.table, name='table'),
    path('forms/', views.forms, name='forms'),
    path('charts/', views.charts, name='charts'),
    path('widgets/', views.widgets, name='widgets'),
]

