from django.db import models
from django.utils.translation import gettext_lazy as _               ## For translations
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.




class Product(models.Model):
    PRDName =  models.CharField(max_length=50, verbose_name=_("Product Name"))
    PRDCategory = models.ForeignKey('Category', on_delete=models.CASCADE,blank=True, null=True ,verbose_name=_("Category"))
    PRDBrand = models.ForeignKey('settings.Brand', on_delete=models.CASCADE ,blank=True, null=True ,verbose_name=_("Brand"))
    PRDDesc = models.TextField(verbose_name=_("Product Description"))
    PRDImage = models.ImageField(upload_to='product_image/',verbose_name=_("Image") , blank=True , null=True)
    PRDPrice = models.DecimalField(max_digits=8 , decimal_places=2 , verbose_name=_("Price"))
    PRDDiscountPrice = models.DecimalField(max_digits=8 , decimal_places=2 , blank=True, null=True,verbose_name=_("Discount Price"))
    PRDCost = models.DecimalField(max_digits=8 , decimal_places=2 , verbose_name=_("Cost"))
    PRDCreated = models.DateTimeField(auto_now=True , verbose_name=_("Created at"))
    
    PRDSlug = models.SlugField(blank=True, null=True, verbose_name=_("Product URL"))
    PRDISNew = models.BooleanField(default=True ,verbose_name=_("New Product"))
    PRDISBestSeller = models.BooleanField(default=False, verbose_name=_("Best Seller"))


    def save(self, *args, **kwargs):
        if not self.PRDSlug:
            self.PRDSlug =slugify(self.PRDName)

        super(Product , self).save(*args , **kwargs)
    


    class Meta:
            verbose_name = _("Product")
            verbose_name_plural = _("Products")



    def get_absolute_url(self):
        return reverse("product:product_detail", kwargs={"slug": self.PRDSlug})
        


    def __str__(self):
        return self.PRDName

    








class ProductImage(models.Model):
    PRDIProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    PRDIImage = models.ImageField(upload_to='product_image/',verbose_name=_("Image"))


    def __str__(self):
        return str(self.PRDIProduct)








class Category(models.Model):
    CATName = models.CharField(max_length=50 , verbose_name=_('Name'))
    CATParent = models.ForeignKey('self' ,limit_choices_to={'CATParent__isnull':True} , verbose_name=_('MAin Category'),on_delete= models.CASCADE , blank=True, null=True) 
    CATDesc = models.TextField(verbose_name=_('Description'))
    CATImg = models.ImageField(upload_to='category/' ,verbose_name=_('Image'),blank=True, null=True)
    CATSlug = models.SlugField(blank=True, null=True, verbose_name=_("Category URL"))


    def save(self, *args, **kwargs):
        if not self.CATSlug:
            self.CATSlug =slugify(self.CATName)

        super(Category , self).save(*args , **kwargs)
    

    class Meta:
            verbose_name = _("Category")
            verbose_name_plural = _("Categories")


    def get_absolute_url(self):
        return reverse("product:category_detail", kwargs={"slug": self.CATSlug})
    


    def __str__(self):
        return self.CATName
    









class Product_Alternative(models.Model):
    PALNProduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='main_product', verbose_name=_('Product'))
    PALNAlternative = models.ManyToManyField(Product, related_name="alternative_product", verbose_name=_('Alternative'))

    

    class Meta:
        verbose_name = _("Product Alternative")
        verbose_name_plural = _("Product Alternatives")

    def __str__(self):
        return str(self.PALNProduct)

 








class Product_Accessories(models.Model):
    PACCProduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='mainAccessory_product',verbose_name=_('Product'))
    PACCAlternative = models.ManyToManyField(Product, related_name="accessories_product",verbose_name=_('Accessories'))

    

    class Meta:
        verbose_name = _("Product Accessory")
        verbose_name_plural = _("Product Accessories")

    def __str__(self):
        return str(self.PACCProduct)
