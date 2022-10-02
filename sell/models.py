from django.db import models
from Account.models import User

# Create your models here.

class sellModel(models.Model):
    
    PRODUCT_CATEGORIES = [
        ['SEED SELLER','Seed Seller'],
        ['FERTILIZER SELLER','Fertilizer Seller'],
        ['PESTICIDE SELLER','Pesticide Seller'],
    ]
    product_image=models.ImageField(blank=False,null=True)
    seller=models.ForeignKey(User,max_length=100, on_delete=models.CASCADE)
    product_category = models.CharField(choices=PRODUCT_CATEGORIES,max_length=20)
    product_name=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    production_date=models.DateField()
    expiration_date=models.DateField()
    price_per_gram=models.IntegerField(default=0)
    registration_date=models.DateField(auto_now_add=True)