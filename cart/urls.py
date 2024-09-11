from django.urls import path
from .views import ViewCartView, AddToCartView, RemoveFromCartView

app_name = 'cart'

urlpatterns = [
    path('', ViewCartView.as_view(), name='view_cart'),
    path('add/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove/<int:product_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
]