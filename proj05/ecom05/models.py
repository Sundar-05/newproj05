from django.db import models
from django.utils.timezone import now

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100)
    desc=models.CharField(max_length=500)
    launch_date=models.DateField(default=now)