from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('add_dish/', views.add_dish, name='add_dish'),
    path('update_dish/<int:dish_id>/', views.update_dish, name='update_dish'),
    path('orders/', views.orders, name='orders'),
    path('update_order/<int:order_id>/', views.update_order, name='update_order'),
]
