from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.view_cart, name='view_cart'),
]
   

