from django.shortcuts import render
from .models import Product

# Create your views here.




def product_list(request):
    product_list = Product.objects.all()


    context = {'products':product_list}
    return render(request, 'Product/product_list.html', context)
 




def product_detail(request):
    pass