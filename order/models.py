from django.db import models
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    total_price = models.DecimalField(max_digits=8, decimal_places=2 ,verbose_name=_("Total Price"))
    order_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Order Date"))
    invoice_number = models.CharField(max_length=20, unique=True, blank=True, null=True,verbose_name=_("Invoice Number"))


    def save(self, *args, **kwargs):
        if not self.invoice_number:
            # Generate a new invoice number using the InvoiceNumber model
            invoice_number_model, created = InvoiceNumber.objects.get_or_create(pk=1)
            self.invoice_number = invoice_number_model.generate_invoice_number()

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"





class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")

    def get_total_price(self):
        return self.product.PRDPrice * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.PRDName} in Order #{self.order.id}"





class InvoiceNumber(models.Model):
    last_invoice_number = models.IntegerField(default=0)

    def generate_invoice_number(self):
        self.last_invoice_number += 1
        self.save()
        return f'INV-{self.last_invoice_number}'