from django.db import models
from product.models import Variant
from accounts.models import BaseUser
from django.utils import timezone

class Order(models.Model):

    user = models.ForeignKey(BaseUser, verbose_name=' نام کاربر', on_delete=models.CASCADE, related_name='order_user')
    create_at = models.DateTimeField(default=timezone.now())
    get_total_price = models.PositiveIntegerField(verbose_name='قیمت سفارش')

    def __str__(self):
        return f'کاربر:{self.user.username} | شماره سفارش: {self.id}'

    @property
    def get_total_price(self):
        return sum(i.total_price() for i in self.order_items.all())

    class Meta:
    
        verbose_name = 'سفارش'
        verbose_name_plural = ' سفارشات'


class OrderItem(models.Model):

    order = models.ForeignKey(Order, verbose_name=' سفارش', on_delete=models.CASCADE, related_name='order_items')
    variant =  models.ForeignKey(Variant, verbose_name='نام محصول', on_delete=models.CASCADE, related_name='order_supply', unique=True)
    price = models.PositiveIntegerField(verbose_name='قیمت محصول')
    quantity = models.PositiveIntegerField(verbose_name='تعداد محصول')

    def __str__(self):
        return f'کاربر:{self.order.user.username} | شماره سفارش: {self.order.id}'
    

    def size(self):
        return self.variant.size.name
    

    def color(self):
        return self.variant.color.name
    
    @property
    def price(self):
        return self.variant.price

    def total_price(self):
        return self.price * self.quantity

    class Meta:
    
        verbose_name = 'اقلام سفارش'
        verbose_name_plural = ' اقلام سفارشات'
