from django.db import models
from user.models import User


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Cart #{self.id}: {self.quantity} x {self.cate} - {self.id_product}"
