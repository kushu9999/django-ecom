from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product
def home(request):
    # we are fetching products from db to show in home page
    products = Product.objects.all().filter(is_available = True)
    
    context = {
        'products' : products,
    }
    return render(request,'home.html', context)