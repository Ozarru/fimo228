import json
from .models import *


def cookieCart(req):
    try:
        cart = json.loads(req.COOKIES['cart'])
    except:
        cart = {}
    print('Cart:', cart)
    items = []
    order = {
        'get_cart_items': 0,
        'get_cart_total': 0
    }
    cartItems = order['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]['quantity']

            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            item = {
                'product': {'id': product.id,
                            'name': product.name,
                            'price': product.price,
                            'thumbnail': product.thumbnail,
                            },
                'quantity': cart[i]['quantity'],
                'get_total': total
            }

            items.append(item)
        except:
            pass
    return {'cartItems': cartItems, 'order': order, 'items': items}


def cartData(req):
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, is_payed=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(req)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {'cartItems': cartItems, 'order': order, 'items': items}


def guestOrder(req, data):

    print('User is not logged in...')
    print('COOKIES:', req.COOKIES)
    name = data['form']['name']
    email = data['form']['email']

    cookieData = cookieCart(req)
    items = cookieData['items']
    customer, created = Customer.objects.get_or_create(
        email=email,
    )
    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer=customer,
        is_payed=False
    )

    for item in items:
        product = Product.objects.get(id=item['product']['id'])

        orderItem = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity']
        )
    return customer, order
