from django.db import models
from django.utils.translation import gettext_lazy as _               ## For translations

# Create your models here.




class Product(models.Model):
    PRDName =  models.CharField(max_length=50, verbose_name=_("Product Name"))
    # Category
    PRDDesc = models.TextField(verbose_name=_("Product Description"))
    PRDPrice = models.DecimalField(max_digits=8 , decimal_places=2 , verbose_name=_("Price"))
    PRDCost = models.DecimalField(max_digits=8 , decimal_places=2 , verbose_name=_("Cost"))
    PRDCreated = models.DateTimeField(verbose_name=_("Created at"))


    def __str__(self):
        return self.PRDName

    


class ProductImage(models.Model):
    PRDIProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    PRDIImage = models.ImageField(upload_to='product_image/',verbose_name=_("Image"))


    def __str__(self):
        return str(self.PRDIProduct)
