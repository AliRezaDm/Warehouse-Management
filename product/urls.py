from django.urls import path
from . import views

app_name ='product'
urlpatterns = [

    # Supply urls
    path('create_supply/', views.SupplyCreateView.as_view(), name='supply_create'), 
    path('update_supply/<id>', views.SupplyUpdateView.as_view(), name='supply_update'), 
    path('delete_supply/<id>', views.SupplyDeleteView.as_view(), name='supply_delete'),

    # Variant Urls
    path ('', views.VariantListView.as_view(), name='variant_list'),
    path ('detail/<id>', views.VariantDetailView.as_view(), name='variant_detail'),
    path ('create_variant/', views.VariantCreateView.as_view( ), name='variant_create'),

    # Category Urls  
    path('category/', views.CategoryList.as_view(), name='category_list'),
    path('create_category/', views.CategoryCreateView.as_view(), name='category_create' ), 

    # Color Urls
    path('create_color/', views.ColorCreateView.as_view(), name='color_create' ),
    path('color_list/', views.ColorListView.as_view(), name='color_list' ),

    # Size Urls
    path('create_size/', views.SizeCreateView.as_view(), name='size_create' ), 
    path('size_list/', views.SizeListView.as_view(), name='size_list' ), 

    # Search Url
    path ('search/', views.search_view, name='search'),
]
