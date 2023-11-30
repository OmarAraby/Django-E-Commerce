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





class Category(models.Model):
    CATName = models.CharField(max_length=50)
    CATParent = models.ForeignKey('self' ,limit_choices_to={'CATParent__isnull':True} , on_delete= models.CASCADE , blank=True, null=True) 
    CATDesc = models.TextField()
    CATImg = models.ImageField(upload_to='category/')

    class Meta:
            verbose_name = _("Category")
            verbose_name_plural = _("Categories")

    def __str__(self):
        return self.CATName
    






class Product_Alternative(models.Model):
    PALNProduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='main_product')
    PALNAlternative = models.ManyToManyField(Product, related_name="alternative_product")

    

    class Meta:
        verbose_name = _("Product Alternative")
        verbose_name_plural = _("Product Alternatives")

    def __str__(self):
        return self.name

 



 
