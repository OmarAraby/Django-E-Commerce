# order/views.py
from django.shortcuts import render, redirect
from .models import Order, OrderItem
from cart.cart import Cart
from product.models import Product


def order_detail(request):

  return render(request, 'order_detail.html', {})




def create_order(request):
    if request.user.is_authenticated:
        # Get the user's cart using the Cart class
        user_cart = Cart(request)

        # Create a new order
        order = Order.objects.create(user=request.user, total_price=user_cart.get_all_total_prices())

        # Add ordered products to the order
        for product in user_cart.get_prods():
            OrderItem.objects.create(order=order, product=product, quantity=user_cart.cart[product.PRDSlug])

        # Clear the user's cart after creating the order
        user_cart.cart.clear()
        user_cart.session.modified = True

        return render(request, 'order_confirmation.html', {'order': order})
    else:
        # Handle the case where the user is not authenticated
        return redirect('login')  # Redirect to the login page or handle authentication as needed
