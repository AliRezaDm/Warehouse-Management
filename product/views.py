from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.db.models.base import Model as Model

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Variant, Supply, Category


class VariantListView(ListView):

    model = Variant
    template_name = 'product/variant_list.html'

class VariantDetailView(DetailView):

    model = Variant
    template_name = 'product/variant_detail.html'

    def get_object(self):
        self.kwargs.get('id')
        return get_object_or_404(Variant.objects.all(), pk=id)




class CategoryList(ListView):

    model = Category
    queryset = Category.objects.filter(status=True)
    template_name = "product/category_list"

class CategoryCreateView(CreateView):

    model = Category
    fields = ['parent', 'title', 'status']
    template_name = "product/add_category_form.html"

class CategoryUpdateView(UpdateView):

    model = Category
    fields = ['parent', 'title', 'status']
    template_name = "product/add_category_form.html"

class CategoryDeleteView(DeleteView):

    model = Category
    success_url = reverse_lazy('product:category_list')