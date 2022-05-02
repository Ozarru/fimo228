from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.http import HttpResponse
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


def cart(req):
    products = Product.objects.all()
    context = {'products': products}
    return render(req, 'shop/cart.html', context)


def checkout(req):
    products = Product.objects.all()
    context = {'products': products}
    return render(req, 'shop/checkout.html', context)
