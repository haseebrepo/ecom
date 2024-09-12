import pdb

from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render
from .cart import get_or_create_cart, add_to_cart, remove_from_cart, get_cart_items

class ViewCartView(TemplateView):
    template_name = 'cart/view_cart.html'

    def get(self, request, *args, **kwargs):
        cart_items = get_cart_items(request)
        # if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        #     return render(request, 'cart/cart_items.html', {'cart_items': cart_items})
        return render(request, 'cart/cart_items.html', {'cart_items': cart_items})

class AddToCartView(View):
    def post(self, request):
        quantity = int(request.POST.get('quantity', 1))
        add_to_cart(request, request.POST.get('productId'), quantity)
        return redirect('cart:view_cart')

class RemoveFromCartView(View):
    def post(self, request):
        product_id = request.POST.get("productId")
        remove_from_cart(request, product_id)
        return redirect('cart:view_cart')

