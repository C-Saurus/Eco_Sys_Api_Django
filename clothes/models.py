from djongo import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    size = models.CharField(max_length=20)
    image = models.ImageField(upload_to="img/clothes_images/")
    material = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
