import pymysql

def fetch_data_from_mysql():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='tiger',
        db='sample_db'
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, price FROM products")
            rows = cursor.fetchall()
            return rows
    finally:
        connection.close()
from django.shortcuts import render
from .integration_logic import fetch_data_from_mysql
def product_list_view(request):
    # Fetch data from MySQL
    products = fetch_data_from_mysql()
    
    # Pass the fetched data to the template
    return render(request, 'product_list.html', {'products': products})
