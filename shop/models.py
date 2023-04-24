from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=1000)
    description=models.CharField(max_length=400)
    category=models.CharField(max_length=50,default="")
    pub_date=models.DateField()
    image = models.ImageField(upload_to='shop/images',default="")
    price = models.DecimalField(max_digits=8, decimal_places=2,default=0)

    def __str__(self):
        return self.product_name