from django.shortcuts import render
from .models import Product
from django.views import View


class ProductView(View):

    def get(self, request):
        products = Product.objects.all()
        return render(request, 'product/products_list.html', {'products': products})