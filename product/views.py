from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.db.models.base import Model as Model
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.decorators.http import require_POST

from .models import Variant, Supply, Category, Color, Size
from . import forms



class SupplyCreateView(CreateView):

    model = Supply
    fields = ['title', 'category', 'image', 'status', 'description']
    template_name = 'product/add_supply_form.html'

class SupplyUpdateView(UpdateView):

    model = Supply
    fields = ['title', 'category', 'image', 'status', 'description']
    template_name = 'product/update_supply_form.html'
    
    def get_object(self):
        global id
        id = self.kwargs.get('id')
        return get_object_or_404(Supply.objects.Available(), pk=id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = id 
        return context

class SupplyDeleteView(DeleteView):

    model = Supply
    success_url = reverse_lazy('product:supply_list')
    template_name = 'product/delete_confirm_supply.html'

    def get_object(self):
        global id 
        id = self.kwargs.get('id')
        return get_object_or_404(Supply.objects.Available(), pk=id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = id 
        return context


#---------------------------------------------------------------------------------
# Variant view -> CreateView, UpdateView, DeleteVeiw, ListView
class VariantListView(ListView):

    model = Variant
    template_name = 'product/variant_list.html'

class VariantDetailView(DetailView):

    model = Variant
    template_name = 'product/variant_detail.html'

    def get_object(self):

        id = self.kwargs.get('id')
        return get_object_or_404(Variant.objects.all(), pk=id)

class VariantCreateView(CreateView):
    model = Variant
    # fields = ['supply', 'color', 'size', 'count']
    template_name = 'product/add_variant_form.html'
    form_class = forms.VariantAddForm

class VariantDeleteView(DeleteView):

    model = Variant
    success_url = reverse_lazy('product:variant_list')
    template_name = 'product/delete_confirm_variant.html'

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Supply.objects.all(), pk=id)
    
class VariantUpdateView(UpdateView):
    model = Variant
    fields = ['supply', 'color', 'size', 'count']
    template_name = 'product/update_variant_form.html'

    def get_object(self):
        global id 
        id = self.kwargs.get('id')
        return get_object_or_404(Variant.objects.all(), pk=id)
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['id'] = id 
        return context 
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

class CategoryDeleteView(DeleteView):

    model = Variant
    success_url = reverse_lazy('product:variant_list')
    template_name = 'product/delete_confirm_category.html'

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Category.objects.all(), pk=id)
    

class CategoryUpdateView(UpdateView):

    model = Category
    fields = ['parent', 'title', 'status']
    template_name = "product/update_category_form.html"
    
    def get_object(self):
        global id 
        id = self.kwargs.get('id')
        return get_object_or_404(Category.objects.all(), pk=id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = id 
        return context
    

#---------------------------------------------------------------------------------
# Size view -> CreateView, UpdateView, ListView, DeleteView
class SizeCreateView(CreateView):

    model = Size
    fields = ['name']
    template_name = "product/add_size_form.html"

class SizeUpdateView(UpdateView):

    model = Size
    fields = ['name']
    template_name = "product/update_size_form.html"

    def get_object(self):
        global id
        id = self.kwargs.get('id')
        return get_object_or_404(Size.objects.all(), pk=id)
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = id 
        return context
    
class SizeListView(ListView):
    
    model = Size
    template_name = 'product/size_list.html'
    queryset = Size.objects.all()

class SizeDeleteView(DeleteView):

    model = Variant
    success_url = reverse_lazy('product:variant_list')
    template_name = 'product/delete_confirm_size.html'

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Size.objects.all(), pk=id)
    
#---------------------------------------------------------------------------------
# Color view -> CreateView, UpdateView, ListView, DeleteView
class ColorCreateView(CreateView):

    model = Color
    fields = ['name']
    template_name = "product/add_color_form.html"

class ColorUpdateView(UpdateView):

    model = Color
    fields = ['name']
    template_name = "product/update_color_form.html"

    def get_object(self):
        global id 
        id = self.kwargs.get('id')
        return get_object_or_404(Color.objects.all(), pk=id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = id 
        return context
    
class ColorListView(ListView):
    
    model = Color
    template_name = 'product/color_list.html'
    queryset = Color.objects.all()

class ColorDeleteView(DeleteView):

    model = Variant
    success_url = reverse_lazy('product:variant_list')
    template_name = 'product/delete_confirm_color.html'

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Color.objects.all(), pk=id)
    
#---------------------------------------------------------------------------------
# SearchView
@require_POST
def search_view(request):
    """
    this view gets search phrase from input in template named query via method POST
    and checks if there is match in Category.title
    """
    variant_query =Variant.objects.Available()
    if request.method == "POST":
        search = request.POST.get('query')
        variant = variant_query.filter(title__icontains = search)
        return render(request, 'product/search_result.html', {"variant": variant})






