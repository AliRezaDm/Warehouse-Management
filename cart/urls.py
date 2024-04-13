from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('', views.CartListView.as_view(), name='cart_detail'),
    path('add', views.cart_add, name='add'),
    path('remove', views.cart_remove, name='remove'),
    path('clear', views.cart_remove, name='clear'),
]
