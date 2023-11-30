from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Brand(models.Model):

    BRDNAme = models.CharField(max_length=50)
    BRDDesc =  models.TextField(blank=True , null=True)

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.BRDNAme

class Variant(models.Model):

    VARNAme = models.CharField(max_length=50)
    VARDesc =  models.TextField(blank=True , null=True)

    

    class Meta:
        verbose_name = _("Variant")
        verbose_name_plural = _("Variants")

    def __str__(self):
        return self.VARNAme

