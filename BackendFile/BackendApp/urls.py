from django.urls import path
from .views import LoginView, RegisterView
from .views import AddToCartView, CartItemListView




urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('cart/add/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartItemListView.as_view(), name='cart_items'),


]

