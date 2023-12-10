from django.shortcuts import render , get_object_or_404
from .cart import Cart
from product.models import Product
from django.http import JsonResponse
# Create your views here.


def cart_summery(request):

	return render(request, 'cart_summery.html' ,{})



def cart_add(request):
	# get the cart
	cart = Cart(request)
	#test for Post
	if request.POST.get('action') == 'post' :
		# Get Stuff
		product_id = int(request.POST.get('product_id')) 

		# Lookup Product in DB
		product = get_object_or_404(Product, id=product_id)

		# save to session 
		cart.add(product=product)

		

		# Return Response
		response = JsonResponse({'Product Name':product.PRDName})
		return response



def cart_delete(request):
	pass



def cart_update(request):
	pass