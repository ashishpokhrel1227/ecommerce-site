from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView, 
    HomeView, 
    OrderSummaryView,
    add_to_cart,
    add_single_item_to_cart,
    remove_from_cart, 
    remove_single_item_from_cart,
    OrderedItem
) 


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('ordered-items', OrderedItem.as_view(), name='ordered-items'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-single-item-to-cart/<slug>/', add_single_item_to_cart, name='add-single-item-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
]