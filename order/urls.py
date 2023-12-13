from django.urls import path
from . import views


app_name='order'

urlpatterns = [
    path('confirmed/', views.create_order, name='confirmed_order'),
    path('detail/<int:order_id>/', views.order_detail, name='order_detail'),
    # path('download_receipt/<int:order_id>/', views.generate_invoice_pdf, name='download_receipt'),
]