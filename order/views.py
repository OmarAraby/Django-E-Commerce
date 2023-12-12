# order/views.py
from django.shortcuts import render, redirect
from .models import Order, OrderItem
from cart.cart import Cart
from product.models import Product
from django.http import HttpResponse
from django.template.loader import render_to_string , get_template
from xhtml2pdf import pisa
from io import BytesIO
from django.utils.text import slugify
import locale




def order_detail(request):
    # Get The Product From Cart To Order view
    user_cart = Cart(request)
    cart_products = user_cart.get_prods()
    quantity = user_cart.get_quants()
    all_total_price = user_cart.get_all_total_prices()
    single_total_price = user_cart.get_single_total_price()
    order = Order.objects.create(user=request.user, total_price=user_cart.get_all_total_prices())


    context = {
            'cart_products':cart_products,
            'quantity':quantity,
            'single_total_price':single_total_price,
            'all_total_price':all_total_price,
            'order':order,
            }

    return render(request, 'order_detail.html', context)




def create_order(request):
    if request.user.is_authenticated:
        # Get the user's cart using the Cart class
        user_cart = Cart(request)
        cart_products = user_cart.get_prods()
        quantity = user_cart.get_quants()
        all_total_price = user_cart.get_all_total_prices()
        single_total_price = user_cart.get_single_total_price()

        # Create a new order
        order = Order.objects.create(user=request.user, total_price=user_cart.get_all_total_prices())

        # Add ordered products to the order
        for product in user_cart.get_prods():
            OrderItem.objects.create(order=order, product=product, quantity=user_cart.cart[product.PRDSlug])

        # Clear the user's cart after creating the order
        user_cart.cart.clear()
        user_cart.session.modified = True

        context = {
            'cart_products':cart_products,
            'quantity':quantity,
            'single_total_price':single_total_price,
            'all_total_price':all_total_price,
            'order':order,
        }

        return render(request, 'order_confirmation.html', context)
    else:
        # Handle the case where the user is not authenticated
        return redirect('login')  # Redirect to the login page or handle authentication as needed













# HAndle to download Invoice







# def render_to_pdf(template_src, context_dict={}):
#     template = get_template('invoice.html')
#     html = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
#     if pdf.err:
#         return HttpResponse("Invalid PDF", status=400, content_type='text/plain')
#     return HttpResponse(result.getvalue(), content_type='application/pdf')



# def generate_invoice_pdf(request, order_id):
#    # Get The Product From Cart To Order view
#     user_cart = Cart(request)
#     cart_products = user_cart.get_prods()
#     quantity = user_cart.get_quants()
#     all_total_price = user_cart.get_all_total_prices()
#     single_total_price = user_cart.get_single_total_price()
#     order = Order.objects.create(user=request.user, total_price=user_cart.get_all_total_prices())
#     user_cart = Cart(request)

#     if not order:
#         return HttpResponse("Order not found", status=404)

#     context = {
#             'cart_products':cart_products,
#             'quantity':quantity,
#             'single_total_price':single_total_price,
#             'all_total_price':all_total_price,
#             'order':order,
#             }
#     response = render_to_pdf("invoice.html", context)

#     if response.status_code == 400:
#         return HttpResponse("Error generating PDF", status=500)

#     filename = f"Invoice_{order.invoice_number}.pdf"
#     content = f"inline; filename={filename}"
#     download = request.GET.get("download")

#     if download:
#         content = f"attachment; filename={filename}"

#     response["Content-Disposition"] = content
#     return response
#     