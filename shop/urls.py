from django.urls import path, include
from .views import *
# from . import views
# app_name = 'shop'
urlpatterns = [
    # ---class shinanigans
    # path('', ProductListView.as_view(), name='products'),
    path('', products, name='products'),
    path('cart/', cart, name='cart'),
    path('factos/', factos, name='factos'),
    path('checkout/', checkout, name='checkout'),
    path('update_item/', updateItem, name='update_item'),
    path('process_order/', processOrder, name='process_order'),
    path('<str:slug>/', ProductDetailView.as_view(),
         name='product-detail'),
]
