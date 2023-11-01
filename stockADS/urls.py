from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search-product/', views.search_product, name='search-product'),
    path('add-product/', views.add_product, name='add_product'),
    path('delete-product/<int:id>/', views.delete_product, name='delete-product'),
    path('product-detail/<int:id>/', views.product_detail, name='product-detail')
]

