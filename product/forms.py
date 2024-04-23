from django import forms
from .models import Size, Color, Category, Variant, Supply

class SupplyAddForm(forms.ModelForm):

    class Meta:
        model = Supply
        fields = ['image', 'category', 'title', 'status', 'description']

class VariantAddForm(forms.ModelForm):

    class Meta:
        model = Variant
        fields = ['supply', 'color', 'size', 'inventory']

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

