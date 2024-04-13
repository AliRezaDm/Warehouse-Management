from django.shortcuts import get_object_or_404
from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Variant


class VariantListView(ListView):

    model = Variant
    template_name = 'product/variant_list.html'

class VariantDetailView(DetailView):

    model = Variant
    template_name = 'product/variant_detail.html'

    def get_object(self):
        self.kwargs.get('id')
        return get_object_or_404(Variant.objects.all(), pk=id)