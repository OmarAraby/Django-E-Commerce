from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product

# Create your views here.




def product_list(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 1)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    product_list = paginator.get_page(page_number)


    context = {'products':product_list}
    return render(request, 'Product/product_list.html', context)
 




def product_detail(request,id):
    product_detail = Product.objects.get(id=id)
    context = {'product_detail':product_detail}
    

    return render(request,'Product/product_detail.html',context)


    