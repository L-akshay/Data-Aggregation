from django.shortcuts import render
from .integration_logic import fetch_data_from_mysql

def product_list_view(request):
    products = fetch_data_from_mysql()
    return render(request, 'product_list.html', {'products': products})
