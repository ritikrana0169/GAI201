from django.shortcuts import render, redirect
from .models import Dish, Order
from .forms import DishForm, OrderForm

def menu_dashboard(request):
    dishes = Dish.objects.all()
    return render(request, 'zomato_app/menu_dashboard.html', {'dishes': dishes})

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'zomato_app/place_order.html', {'form': form})

def order_detail(request, order_id):
    order = Order.objects.get(pk=order_id)
    return render(request, 'zomato_app/order_detail.html', {'order': order})
