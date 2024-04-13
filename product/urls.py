from django.urls import path
from . import views

app_name ='product'
urlpatterns = [
    path ('', views.VariantListView.as_view(), name='variant_list'),
    path ('detail/<id>', views.VariantDetailView.as_view(), name='variant_detail')
]
