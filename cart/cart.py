import pdb
from decimal import Decimal

from django.conf import settings
from product.models import Product

from .models import Cart, CartItem
from django.contrib.sessions.models import Session


def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key

        session = Session.objects.get(session_key=session_key)
        cart, created = Cart.objects.get_or_create(session=session)

    return cart


def add_to_cart(request, product_id, quantity=1):
    cart = get_or_create_cart(request)
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()


def remove_from_cart(request, product_id):
    cart = get_or_create_cart(request)
    CartItem.objects.filter(cart=cart, product_id=product_id).delete()


def get_cart_items(request):
    cart = get_or_create_cart(request)
    return cart.items.all()
