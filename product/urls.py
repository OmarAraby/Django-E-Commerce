from django.urls import path 
from . import views








urlpatterns = [
    path('',views.product_list,name='home'),
    path('<int:id>',views.product_detail ),

    
]