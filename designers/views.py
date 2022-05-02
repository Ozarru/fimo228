
from django.views.generic import ListView, DetailView
from .models import Designer
# class based views---------------------


class DesignerListView(ListView):
    model = Designer
    template_name = 'designers/index.html'
    context_object_name = 'designers'
    # ordering = ['date_posted']


class DesignerDetailView(DetailView):
    model = Designer
