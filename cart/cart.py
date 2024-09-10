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
        cart_item.save()


def remove_from_cart(request, product_id):
    cart = get_or_create_cart(request)
    CartItem.objects.filter(cart=cart, product_id=product_id).delete()


def get_cart_items(request):
    cart = get_or_create_cart(request)
    return cart.items.all()

















"""
class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = Decimal(item['price']) * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_sub_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item
                   in self.cart.values())

    def clear(self):
        for key in list(self.cart.keys()):
            del self.cart[key]
        self.save()

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price),
                                     'name': str(product.name)
                                     }
            self.save()
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
            self.save()
        else:
            self.cart[product_id]['quantity'] += quantity
            self.save()


    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def save(self):
        self.session.modified = True
"""