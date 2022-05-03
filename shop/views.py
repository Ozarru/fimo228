import json
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
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
    # products = Product.objects.all()
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    products = Product.objects.filter(
        Q(couture__name__icontains=query) | Q(name__icontains=query) | Q(collection__icontains=query))
    coutures = Couture.objects.all()
    context = {'products': products, 'coutures': coutures}

    return render(req, 'shop/index.html', context)


def factos(req):
    return render(req, 'shop/factos.html')


def cart(req):
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, is_payed=False)
        cart_items = order.orderitem_set.all()
    else:
        cart_items = []
        order = {
            'get_cart_items': 0,
            'get_cart_total': 0
        }
    context = {'cart_items': cart_items, 'order': order, 'title': 'cart'}
    return render(req, 'shop/cart.html', context)


def checkout(req):
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, is_payed=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': order, 'title': 'checkout'}
    return render(req, 'shop/checkout.html', context)


def updateItem(req):
    data = json.loads(req.body)
    productId = data.productId
    action = data.action
    print('Product :', productId)
    print('Action :', action)

    customer = req.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)
