from django.urls import path
from . import views

urlpatterns = [
    path('',views.store, name='store'),
    path('<slug:category_slugg>/',views.store, name='products_by_category')
] 

