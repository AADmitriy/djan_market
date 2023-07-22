from django.urls import path

from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('contacts/', views.contacts, name='contacts'),
    path('products/', views.products, name='products'),
    path('products/food/', views.food_products, name='food_products'),
    path('products/drinks/', views.drinks_products, name='drinks_products'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_product/success', views.success, name='success'),
]