from django import forms
from .models import Size, Type, Category, Variant, Supply

class SupplyAddForm(forms.ModelForm):

    class Meta:
        model = Supply
        fields = ['image', 'category', 'title', 'status', 'description']

class VariantAddForm(forms.ModelForm):

    class Meta:
        model = Variant
        fields = ['supply', 'type', 'size', 'price', 'inventory']

class CategoryAddForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['id', 'parent', 'position', 'title', 'status']

class TypeAddForm(forms.ModelForm):

    class Meta:
        model = Type
        fields = ['name']

class SizeAddForm(forms.ModelForm):

    class Meta:
        model = Size
        fields = ['name']

