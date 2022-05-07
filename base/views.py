from django.shortcuts import render

from shop.utils import cartData


def home(req):
    data = cartData(req)
    cartItems = data['cartItems']
    context = {"title": 'acceuill', 'cartItems': cartItems}
    return render(req, 'base/index.html', context)


def agency(req):
    data = cartData(req)
    cartItems = data['cartItems']
    context = {"title": 'agence', 'cartItems': cartItems}
    return render(req, 'base/agency.html', context)
