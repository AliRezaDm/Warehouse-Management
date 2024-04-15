from django.urls import path
from . import views

app_name ='product'
urlpatterns = [

    # Supply urls
    path('create_supply/', views.SupplyCreateView.as_view(), name='supply_create'), 
    path('update_supply/<int:id>', views.SupplyUpdateView.as_view(), name='supply_update'), 
    path('delete_supply/<int:id>', views.SupplyDeleteView.as_view(), name='supply_delete'),

    # Variant Urls
    path ('', views.VariantListView.as_view(), name='variant_list'),
    path ('detail/<int:id>', views.VariantDetailView.as_view(), name='variant_detail'),
    path ('create_variant/', views.VariantCreateView.as_view( ), name='variant_create'),
    path ('update_variant/<int:id>', views.VariantUpdateView.as_view( ), name='variant_update'),
    path ('delete_variant/<int:id>', views.VariantDeleteView.as_view( ), name='variant_delete'),

    # Category Urls  
    path('category/', views.CategoryList.as_view(), name='category_list'),
    path('create_category/', views.CategoryCreateView.as_view(), name='category_create' ), 
    path('update_category/<int:id>', views.CategoryUpdateView.as_view(), name='category_update' ), 
    path('delete_category/<int:id>', views.CategoryDeleteView.as_view(), name='category_delete' ), 

    # Color Urls
    path('create_color/', views.ColorCreateView.as_view(), name='color_create' ),
    path('color_list/', views.ColorListView.as_view(), name='color_list' ),
    path('update_color/<int:id>', views.ColorUpdateView.as_view(), name='color_update' ),
    path('delete_color/<int:id>', views.ColorDeleteView.as_view(), name='color_delete' ),


    # Size Urls
    path('create_size/', views.SizeCreateView.as_view(), name='size_create' ), 
    path('size_list/', views.SizeListView.as_view(), name='size_list' ), 
    path('update_size/<int:id>', views.SizeUpdateView.as_view(), name='size_update' ), 
    path('delete_size/<int:id>', views.SizeDeleteView.as_view(), name='size_delete' ), 


    # Search Url
    path ('search/', views.search_view, name='search'),
]
