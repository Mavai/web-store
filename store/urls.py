from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:product_id>/', views.show, name='show'),
  path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
  path('cart/', views.cart, name='cart'),
  path('cart/delete', views.delete_from_cart, name='delete-from-cart')
]