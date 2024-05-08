from django.db import models
from product.models import Variant
from accounts.models import BaseUser
from django.utils import timezone

class Cart(models.Model):

    user = models.ForeignKey(BaseUser, verbose_name=' نام کاربر', on_delete=models.CASCADE, related_name='cart_user')
    create_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f' کاربر:{self.user.username} '

    @property
    def get_total_price(self):
        return sum(i.total_price() for i in self.cart_items.all())

    class Meta:
    
        verbose_name = 'سبد خرید'
        verbose_name_plural = ' سبد خرید'

class CartItem(models.Model):

    cart = models.ForeignKey(Cart, verbose_name=' سبد خرید', on_delete=models.CASCADE, related_name='cart_items')
    variant =  models.ForeignKey(Variant, verbose_name='نام محصول', on_delete=models.CASCADE, related_name='cart_supply', unique=True)
    quantity = models.PositiveIntegerField(verbose_name='تعداد محصول')

    def __str__(self):
        return f' کاربر:{self.cart.user.username} '
    

    def size(self):
        return self.variant.size.name
    

    def type(self):
        return self.variant.type.name
    
    def price(self):
        return self.variant.price

    def total_price(self):
        return self.variant.price * self.quantity

    class Meta:
        verbose_name = 'اقلام سبد خرید'
        verbose_name_plural = ' اقلام سبد خرید'
