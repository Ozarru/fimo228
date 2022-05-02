from re import template
from django.urls import path, include
from . import views
from .views import MannequinListView, MannequinDetailView
# app_name = 'mannequins'
urlpatterns = [
    # ---class shinanigans
    path('', MannequinListView.as_view(), name='mannequins'),
    path('<str:slug>/', MannequinDetailView.as_view(
        template_name='mannequins/detail.html'), name='mannequin-detail'),
]
