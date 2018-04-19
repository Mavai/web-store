from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Item
from decimal import Decimal


def index(request):
    sort = request.GET.get('sort')
    order = request.GET.get('order')
    if (sort == 'name' or sort == 'code' or sort == 'price'):
        if order == 'desc':
            items = Item.objects.order_by('-' + sort)
        else:
            items = Item.objects.order_by(sort)
    else:
        items = Item.objects.all()
    context = {'items': items, 'sum': request.session.get('sum', 0)}
    return render(request, 'store/index.html', context)


def show(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {'item': item, 'sum': request.session.get('sum', 0)}
    return render(request, 'store/show.html', context)


def cart(request):
    cart = request.session.get('cart', {})
    items_in_cart = Item.objects.filter(id__in=cart.keys()).values()
    for item in items_in_cart:
        item['count'] = cart[str(item['id'])]
    context = {'cart': items_in_cart, 'sum': request.session.get('sum', 0)}
    return render(request, 'store/cart.html', context)

def delete_from_cart(request):
    cart = request.session['cart']
    item_id = request.POST.get('id')
    item = Item.objects.get(id = item_id)
    count = request.POST.get('count')
    cart[item_id] = cart[item_id] - int(count)
    if cart[item_id] == 0:
        del cart[item_id]
    sum = Decimal(request.session['sum'])
    request.session['sum'] = str(sum - int(count) * item.price)
    request.session['cart'] = cart
    return redirect('cart')


def add_to_cart(request):
    cart = request.session.get('cart', {})
    item_id = request.GET.get('id')
    count = int(request.GET.get('count'))
    if item_id not in cart:
        cart[item_id] = count
    else:
        cart[item_id] = cart[item_id] + count
    request.session['cart'] = cart
    item = Item.objects.get(id = item_id)
    sum = Decimal(request.session.get('sum', 0)) + count * item.price
    request.session['sum'] = str(sum)
    data = { 'sum': sum }
    return JsonResponse(data)
