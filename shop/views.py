from datetime import datetime
import json
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from .utils import cookieCart, cartData, guestOrder
from .models import *

# class based views---------------------


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/index.html'
    ordering = ['date_added']


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/detail.html'

# ------------------------------------


def products(req):
    data = cartData(req)
    cartItems = data['cartItems']

    # products = Product.objects.all()
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    products = Product.objects.filter(
        Q(couture__name__icontains=query) | Q(name__icontains=query) | Q(collection__icontains=query))
    coutures = Couture.objects.all()
    context = {'products': products,
               'coutures': coutures, 'cartItems': cartItems, 'title': 'boutique'}

    return render(req, 'shop/index.html', context)


def orders(req):
    data = cartData(req)
    cartItems = data['cartItems']

    # products = Product.objects.all()
    # query = req.GET.get('query') if req.GET.get('query') != None else ''
    orders = Order.objects.all()
    context = {'orders': orders, 'cartItems': cartItems, 'title': 'orders'}
    return render(req, 'shop/orders.html', context)


def cart(req):
    data = cartData(req)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order,
               'cartItems': cartItems, 'title': 'panier'}
    return render(req, 'shop/cart.html', context)


def checkout(req):
    data = cartData(req)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order,
               'cartItems': cartItems, 'title': 'checkout'}
    return render(req, 'shop/checkout.html', context)


def updateItem(req):
    data = json.loads(req.body)
    productId = data['productId']
    action = data['action']
    print('Product :', productId)
    print('Action :', action)

    customer = req.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, is_payed=False)
    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added or removed', safe=False)


def clearCart(cart):
    for items in cart:
        items.delete()
        print('cart cleared')


def processOrder(req):
    transaction_id = datetime.now().timestamp()
    data = json.loads(req.body)

    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, is_payed=False)

    else:
        customer, order = guestOrder(req, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.is_payed = True
    order.save()

    ShippingInfo.objects.create(
        customer=customer,
        order=order,
        phone=data['shipping']['phone'],
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        country=data['shipping']['country'],
    )

    return JsonResponse('Payment complete', safe=False)
