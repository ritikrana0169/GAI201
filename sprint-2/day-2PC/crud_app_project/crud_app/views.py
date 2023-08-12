from django.shortcuts import render, redirect

data_storage = {}

def create_view(request):
    if request.method == 'POST':
        key = request.POST['key']
        value = request.POST['value']
        data_storage[key] = value
        return redirect('read')
    return render(request, 'create.html')

def read_view(request):
    return render(request, 'read.html', {'data_storage': data_storage})

def update_view(request):
    if request.method == 'POST':
        key = request.POST['key']
        value = request.POST['value']
        if key in data_storage:
            data_storage[key] = value
        return redirect('read')
    return render(request, 'update.html')

def delete_view(request):
    if request.method == 'POST':
        key = request.POST['key']
        if key in data_storage:
            del data_storage[key]
        return redirect('read')
    return render(request, 'delete.html')
