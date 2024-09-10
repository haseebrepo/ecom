from django.views.generic import TemplateView, View
from django.shortcuts import redirect
from django.contrib import messages
from .cart import get_or_create_cart, add_to_cart, remove_from_cart, get_cart_items

class ViewCartView(TemplateView):
    template_name = 'cart/view_cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_items'] = get_cart_items(self.request)
        return context

class AddToCartView(View):
    def post(self, request, product_id):
        quantity = int(request.POST.get('quantity', 1))
        add_to_cart(request, product_id, quantity)
        messages.success(request, "Item added to cart successfully.")
        return redirect('cart:view_cart')

class RemoveFromCartView(View):
    def post(self, request, product_id):
        remove_from_cart(request, product_id)
        messages.success(request, "Item removed from cart successfully.")
        return redirect('cart:view_cart')









"""
from django.shortcuts import render, redirect
from .cart import get_or_create_cart, add_to_cart, remove_from_cart, get_cart_items

def view_cart(request):
    cart_items = get_cart_items(request)
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items})

def add_to_cart_view(request, product_id):
    quantity = int(request.POST.get('quantity', 1))
    add_to_cart(request, product_id, quantity)
    return redirect('cart:view_cart')

def remove_from_cart_view(request, product_id):
    remove_from_cart(request, product_id)
    return redirect('cart:view_cart')

"""


















"""
import pdb

from django.shortcuts import render

# Create your views here.





from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from product.models import Product
from .cart import Cart
import json


@method_decorator(csrf_exempt, name='dispatch')
class CartView(View):
    def get(self, request, product_id=None):


        if request.GET.get('add'):
            self.post(request, product_id=product_id)
        # elif request.GET.get('remove'):
        #     self.delete(request)
        cart = Cart(request)
        print('here is cart: ', cart)
        return render(request, 'cart/cart_detail.html', {'cart_items': cart.cart, 'total_price': 0})

    def post(self, request, product_id=None):
        cart = Cart(request)
        # data = Product.objects.get(id=product_id)
        # product_id = data.get('product_id')
        # quantity = data.get('quantity', 1)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        # cart.add(product=product, quantity=quantity, override_quantity=False)

        # return JsonResponse({'message': 'Product added to cart', 'cart_total': len(cart)})

    def put(self, request, product_id=None):
        cart = Cart(request)
        data = json.loads(request.body)
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=quantity, override_quantity=True)
        # return JsonResponse({'message': 'Cart updated', 'cart_total': len(cart)})

    def delete(self, request, product_id=None):
        cart = Cart(request)
        data = json.loads(request.body)
        product_id = data.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return JsonResponse({'message': 'Product removed from cart', 'cart_total': len(cart)})

class ClearCartView(View):
    def post(self, request):
        cart = Cart(request)
        cart.clear()
        return JsonResponse({'message': 'Cart cleared', 'cart_total': 0})

"""