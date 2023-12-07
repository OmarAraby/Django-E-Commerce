from django.db import models
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("Quantity"))
    order_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Order Date"))

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"{self.user.username} - {self.product.PRDName}"