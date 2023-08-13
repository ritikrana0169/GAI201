from django.shortcuts import render
from django.http import JsonResponse

# Sample data (replace this with your actual data)
menu_items = [
    {'id': 1, 'name': 'Pizza', 'price': 10.99, 'availability': True},
    {'id': 2, 'name': 'Burger', 'price': 5.99, 'availability': False},
    # Add more menu items
]

orders = []
order_counter = 1

def menu(request):
    return render(request, 'zomato_app/menu.html', {'menu_items': menu_items})

def orders(request):
    return render(request, 'zomato_app/orders.html', {'orders': orders})
 
def add_dish(request):
    if request.method == 'POST':
        dish_id = int(request.POST.get('dish_id'))
        dish = next(item for item in menu_items if item['id'] == dish_id)
        orders.append({'order_id': order_counter, 'dish': dish, 'status': 'received'})
        global order_counter
        order_counter += 1
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def update_order(request, order_id):
    if request.method == 'POST':
        new_status = request.POST.get('status')
        for order in orders:
            if order['order_id'] == order_id:
                order['status'] = new_status
                break
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
