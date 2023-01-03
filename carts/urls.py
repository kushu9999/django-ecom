from django.urls import path
from . import views
urlpatterns = [
    path('', views.cart, name='cart'),
    path('addcart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('removecart/<int:product_id>/', views.remove_cart, name='remove_cart'),
    path('removecartitem/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
]