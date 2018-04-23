from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Product
from decimal import Decimal
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q


def index(request):
    sort = request.GET.get('sort')
    order = request.GET.get('order')
    filter = request.GET.get('filter', '')
    products = sorted_products(sort, order, filter)
    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    products_to_show = paginator.get_page(page)
    queries_without_filter = request.GET.copy()
    if 'filter' in queries_without_filter:
        del queries_without_filter['filter']
    context = {
        'products': products_to_show,
        'queries': queries_without_filter,
        'params': request.GET.urlencode,
        'sum': request.session.get('sum', 0)
    }
    return render(request, 'store/index.html', context)


def show(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product, 'sum': request.session.get('sum', 0)}
    return render(request, 'store/show.html', context)


def cart(request):
    cart = request.session.get('cart', {})
    products_in_cart = Product.objects.filter(id__in=cart.keys()).values()
    for product in products_in_cart:
        product['count'] = cart[str(product['id'])]
        product['total_price'] = product['price'] * cart[str(product['id'])]
    context = {'cart': products_in_cart, 'sum': request.session.get('sum', 0)}
    return render(request, 'store/cart.html', context)


def delete_from_cart(request):
    product_id = request.POST.get('id')
    count = int(request.POST.get('count'))
    cart = request.session['cart']
    product = Product.objects.get(id=product_id)
    cart[product_id] = cart[product_id] - count
    if cart[product_id] <= 0:
        del cart[product_id]
    request.session['cart'] = cart
    update_total_sum(request, product, count, 'remove')
    messages.add_message(request, messages.SUCCESS,
                         'Removed {0} ({1}) from cart.'.format(product.name, count))
    return redirect('cart')


def add_to_cart(request):
    product_id = request.GET.get('id')
    count = int(request.GET.get('count'))
    cart = request.session.get('cart', {})
    if count <= 0:
        return HttpResponseBadRequest
    if product_id not in cart:
        cart[product_id] = count
    else:
        cart[product_id] = cart[product_id] + count
    request.session['cart'] = cart
    product = Product.objects.get(id=product_id)
    update_total_sum(request, product, count, 'add')
    data = {'sum': request.session.get(
        'sum'), 'product': product.name, 'count': count}
    return JsonResponse(data)


def sorted_products(sort, order, filter):
    products = Product.objects.filter(
        Q(name__contains=filter) | Q(code__contains=filter))
    if (sort == 'name' or sort == 'code' or sort == 'price' or sort == '-price'):
        products = products.order_by(sort)
    return products


def update_total_sum(request, product, count, operation):
    sum = Decimal(request.session.get('sum', 0))
    if (operation == 'add'):
        new_sum = sum + count * product.price
    else:
        new_sum = sum - int(count) * product.price
    request.session['sum'] = str(new_sum)
