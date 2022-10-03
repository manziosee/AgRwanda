from functools import total_ordering
from django.db import models
from Account.models import User
from sell.models import sellModel
from django.contrib.auth import get_user

# Create your models here.

User = get_user()

class Order(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    ordered_date=models.DateTimeField(auto_now_add=True)
    
    @property
    def get_cart_total(self):
        global total
        orderedItems=self.sellModel.all()
    

class OrderedProduct(models.Model):
    product=models.ForeignKey(sellModel,max_length=100,on_delete=models.CASCADE)
    quantity_in_grams=models.IntegerField(default=0)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    
    @property
    def products_price(self):
        price=self.product.price_per_gram * self.quantity_in_grams
        return price
    
