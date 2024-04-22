from django.db import models
from carts.models import Item as CartModel


# Create your models here.
class Item:
    id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    order_date = models.DateTimeField()
    total_price = models.DecimalField()
