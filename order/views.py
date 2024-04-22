from typing import Any
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import Cart, CartItem
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin

from product.models import Variant



class CartListView(ListView, LoginRequiredMixin):
    model = CartItem
    template_name = 'cart/cart_list.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["cart_user"] = Cart.objects.get(user=self.request.user)
        return context
    

@require_POST
def add_cart(request):

    url = request.META.get('HTTP_REFERER')
    variant_id = request.POST.get('variant_id')
    variant_quantity = request.POST.get('quantity')

    try:
        cart_user = Cart.objects.get(user=request.user)
        cart_item = CartItem.objects.get(cart=cart_user, variant_id=variant_id)
        variant_quantity = int(variant_quantity)
        cart_item.quantity += variant_quantity
        cart_item.save()
    except Cart.DoesNotExist:
        cart_user = Cart.objects.create(user=request.user)
        variant = get_object_or_404(Variant, id=variant_id)
        CartItem.objects.create(cart=cart_user, variant=variant, quantity=variant_quantity)
    except CartItem.DoesNotExist:
        variant = get_object_or_404(Variant, id=variant_id)
        CartItem.objects.create(cart=cart_user, variant=variant, quantity=variant_quantity)    # cart_user = Cart.objects.filter(user__id=request.user.id)
    # cart_items = CartItem.objects.filter(cart__in=cart_user, variant__id=variant_id)   
    # if cart_items:
    #     cart_items.quantity += variant_quantity 
    #     cart_items.save()
    # else:
    #     cart = Cart.objects.create(user__id=request.user.id)
    #     CartItem.objects.create(cart__id=cart.user.id, variant__id=variant_id, price=variant_id.price, quantity = variant_quantity)

    return HttpResponseRedirect(url)

@require_POST
def remove_cart(request):

    url = request.META.get('HTTP_REFERER')    
    variant_id = request.POST.get('variant_id')
    cart_user = Cart.objects.get(user__id=request.user.id)
    cart_items = CartItem.objects.get(cart__id=cart_user, variant__id=variant_id)

    cart_items.delete()
    
    return HttpResponseRedirect(url)


def clear_cart(request):  
    url = request.META.get('HTTP_REFERER')
    cart_user = Cart.objects.get(user__id=request.user.id)
    cart_user.delete()

    return HttpResponseRedirect(url)