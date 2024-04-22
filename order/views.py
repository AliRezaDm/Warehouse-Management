from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Order, OrderItem
from cart.models import Cart
from product.models import Variant

@login_required()
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    context = {'order':order}
    return render(request, 'order/order.html', context)


@require_POST
@login_required()
def order_create(request):
    order = Order.objects.create(user_id=request.user.id)
    
    cart = Cart(request)
    for item in cart:
        OrderItem.objects.create(order_id=order.id, variant=item['variant'], price=item['price'], quantity=item['quantity'])
        variant = Variant.objects.filter(id= item['variant'].id)
        for data in variant:
            data.count -= item['quantity']
            data.save()
    
    Cart.objects.filter(user_id=request.user.id).delete()
    
    return redirect('order-detail', order.id)
