from django.shortcuts import render, get_object_or_404
from .models import User, Order
from django.http import HttpResponse
from datetime import datetime, timedelta


def index(request):
    return render(request, "homework2_app/base.html")


def basket(request, user_id):
    products = []
    user = User.objects.filter(pk=user_id).first()
    orders = Order.objects.filter(customer=user).all()
    for order in orders:
        products.append(order.products.all())
    products.reverse()
    return render(request, 'homework2_app/user_all_orders.html',
                  {'user': user, 'orders': orders, 'products': products})


def sorted_basket(request, user_id, days_ago):
    product_set = []
    now = datetime.now()
    before = now - timedelta(days=days_ago)
    user = User.objects.filter(pk=user_id).first()
    orders = Order.objects.filter(customer=user, date_ordered__range=(before, now)).all()
    for order in orders:
        products = order.products.all()
        for product in products:
            if product not in product_set:
                product_set.append(product)

    return render(request, 'homework2_app/user_all_product.html',
                  {'user': user, 'product_set': product_set, 'days': days_ago})
