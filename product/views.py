from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.db.models.base import Model as Model
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Variant, Supply, Category, Color, Size


class VariantListView(ListView):

    model = Variant
    template_name = 'product/variant_list.html'

class VariantDetailView(DetailView):

    model = Variant
    template_name = 'product/variant_detail.html'

    def get_object(self):
        self.kwargs.get('id')
        return get_object_or_404(Variant.objects.all(), pk=id)

#---------------------------------------------------------------------------------
# Category view -> CreateView, UpdateView, DeleteVeiw, ListView
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

#---------------------------------------------------------------------------------
# Size view -> CreateView, UpdateView, ListView
class SizeCreateView(CreateView):

    model = Size
    fields = ['name']
    template_name = "product/add_size_form.html"

class SizeUpdateView(UpdateView):

    model = Size
    fields = ['name']
    template_name = "product/add_size_form.html"

class SizeListView(ListView):
    
    model = Size
    template_name = 'product/size_list.html'
    queryset = Size.objects.all()
    
#---------------------------------------------------------------------------------
# Color view -> CreateView, UpdateView, ListView
class ColorCreateView(CreateView):

    model = Color
    fields = ['name']
    template_name = "product/add_color_form.html"

class ColorUpdateView(UpdateView):

    model = Color
    fields = ['name']
    template_name = "product/add_color_form.html"

class ColorListView(ListView):
    
    model = Color
    template_name = 'product/color_list.html'
    queryset = Color.objects.all()







