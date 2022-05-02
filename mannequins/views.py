from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Mannequin
# class based views---------------------


class MannequinListView(ListView):
    model = Mannequin
    template_name = 'mannequins/index.html'
    context_object_name = 'mannequins'
    # ordering = ['date_posted']


class MannequinDetailView(DetailView):
    model = Mannequin
