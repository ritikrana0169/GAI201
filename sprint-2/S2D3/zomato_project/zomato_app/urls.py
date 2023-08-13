from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('orders/', views.orders, name='orders'),
    path('add_dish/', views.add_dish, name='add_dish'),
    path('update_order/<int:order_id>/', views.update_order, name='update_order'),
]
