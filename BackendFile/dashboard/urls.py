from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('table/', views.table, name='table'),
    path('forms/', views.create_menu_item, name='form'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('charts/', views.charts, name='charts'),
    path('widgets/', views.widgets, name='widgets'),
]

