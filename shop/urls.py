from django.urls import path, include
from .views import *
# app_name = 'shop'
urlpatterns = [
    # ---class shinanigans
    path('', ProductListView.as_view(), name='products'),
    path('<str:slug>/', ProductDetailView.as_view(),
         name='product-detail'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
]
