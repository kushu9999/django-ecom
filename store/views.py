from django.shortcuts import get_object_or_404, render
from store.models import Product
from category.models import Category

# Create your views here.

def store(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug != None :
        # it'll get obejct from category, is there not any objects it'll give 404 not found
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available = True)
        product_count = products.count()
    else :
        products = Product.objects.all().filter(is_available = True)
        product_count = products.count()
    
    context = {
        'products' : products,
        'product_count' : product_count,
    }
    return render(request, 'store/store.html' , context)