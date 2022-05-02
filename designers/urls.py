from django.urls import path, include
from . import views
from .views import DesignerListView, DesignerDetailView
# app_name = 'designers'
urlpatterns = [

    path('', DesignerListView.as_view(), name='designers'),
    path('<str:slug>/', DesignerDetailView.as_view(
        template_name='designers/detail.html'), name='designer-detail'),
]
