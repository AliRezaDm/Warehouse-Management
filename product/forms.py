from django import forms
from .models import Size, Color, Category, Variant

class VariantAddForm(forms.ModelForm):

    class Meta:
        model = Variant
        fields = ['product', 'color', 'size', 'count']

class CategoryAddForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['id', 'parent', 'title', 'status']

class ColorAddForm(forms.ModelForm):

    class Meta:
        model = Color
        fields = ['name']

class SizeAddForm(forms.ModelForm):

    class Meta:
        model = Size
        fields = ['name']

