from django.urls import path, include
from . import views

# app_name = 'base'
urlpatterns = [
    path('', views.home, name='home'),
    path('agency/', views.agency, name='agency'),
]
