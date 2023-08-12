import json
from django.shortcuts import render, redirect

def load_data():
    with open('menu_items.json', 'r') as f:
        menu_items = json.load(f)
    with open('orders.json', 'r') as f:
        orders_list = json.load(f)
    return menu_items, orders_list

def save_data(menu_items, orders_list):
    with open('menu_items.json', 'w') as f:
        json.dump(menu_items, f, indent=4)
    with open('orders.json', 'w') as f:
        json.dump(orders_list, f, indent=4)

def menu(request):
    menu_items, _ = load_data()

    if request.method == 'POST':
        name = request.POST['name']
        price = float(request.POST['price'])
        menu_items.append({'name': name, 'price': price})
        save_data(menu_items, [])
        return redirect('menu')
    
    return render(request, 'zomato_app/menu.html', {'menu_items': menu_items})

def add_dish(request):
    return render(request, 'zomato_app/add_dish.html')

def update_dish(request, dish_id):
    menu_items, _ = load_data()

    if request.method == 'POST':
        name = request.POST['name']
        price = float(request.POST['price'])
        menu_items[dish_id] = {'name': name, 'price': price}
        save_data(menu_items, [])
        return redirect('menu')

    return render(request, 'zomato_app/update_dish.html', {'dish': menu_items[dish_id], 'dish_id': dish_id})

def orders(request):
    _, orders_list = load_data()

    if request.method == 'POST':
        order_id = int(request.POST['order_id'])
        new_status = request.POST['status']
        for order in orders_list:
            if order['id'] == order_id:
                order['status'] = new_status
                save_data([], orders_list)
                return redirect('orders')

    return render(request, 'zomato_app/orders.html', {'orders_list': orders_list})
    
def update_order(request, order_id):
    _, orders_list = load_data()

    if request.method == 'POST':
        new_status = request.POST['status']
        for order in orders_list:
            if order['id'] == order_id:
                order['status'] = new_status
                save_data([], orders_list)
                return redirect('orders')

    return render(request, 'zomato_app/update_order.html', {'order_id': order_id})
