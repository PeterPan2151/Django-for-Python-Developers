from django.shortcuts import render

# Create your views here.
def electronics(request):
    product_dict = {
        'product1': 'Mac',
        'product2': 'Iphone',
        'product3': 'Dell Laptop'
    }
    return render(request, 'productApp/products.html', product_dict)

def toys(request):
    product_dict = {
        'product1': 'Remote Car',
        'product2': 'Drone',
        'product3': 'Rocket Launcher'
    }
    return render(request, 'productApp/products.html', product_dict)

def shoes(request):
    product_dict = {
        'product1': 'Nike',
        'product2': 'Adidas',
        'product3': 'Reebok'
    }
    return render(request, 'productApp/products.html', product_dict)

def index(request):
    return render(request, 'productApp/index.html')
