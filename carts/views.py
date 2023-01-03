from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from carts.models import Cart, CartItem
from django.http import HttpResponse
 
# Create your views here.

# we will get session id uding requests if session_key not found we will create a new session
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        # get existing cart by adding session_key
        cart = Cart.objects.get(cart_id=_cart_id(request))

    except Cart.DoesNotExist:
        # if cart not exist, eg. 0 products in cart, then it'll cerate new cart using session_key
        cart = Cart.objects.create(cart_id=_cart_id(request))
    cart.save()  

    try:
        # get existing cart_item by adding product and cart 
        cart_item = CartItem.objects.get(product=product, cart=cart)
        # it'll increase quantiy of cart_item by 1
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        # if cart_item not exist, eg. 0 products in cart, then it'll cerate new product using product and cart 
        cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
        cart_item.save()
    # return HttpResponse(cart_item.quantity)
    return redirect('cart')


def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')


def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity = cart_item.quantity

    except objectNotExist:
        pass # just ignore

    context = {'total':total, 'quantity':quantity, 'cart_items':cart_items, 'tax':round(total*0.18, 2), 'grand_total':round(total*1.18,2)}
    return render(request, 'store/cart.html', context)