from django.urls import path
from .views import ViewCartView, AddToCartView, RemoveFromCartView

app_name = 'cart'

urlpatterns = [
    path('', ViewCartView.as_view(), name='view_cart'),
    path('add/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove/<int:product_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
]




















"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart_view, name='add_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart_view, name='remove_from_cart'),
]
"""






















"""
from django.urls import path
from .views import CartView


urlpatterns = [
    path('cart/', CartView.as_view(), name='cart-view'),
    path('cart/<int:product_id>/', CartView.as_view(), name='cart-view'),
]
"""
