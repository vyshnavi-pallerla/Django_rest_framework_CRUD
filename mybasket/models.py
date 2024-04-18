from django.db import models

# Create your models here.

class Products(models.Model):
    product_name = models.CharField(max_length=300,null = False,blank = False)
    category = models.CharField(max_length=300,null=False,blank=False)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    description = models.TextField()
    ratting = models.IntegerField()

    def __str__(self):
        return self.product_name