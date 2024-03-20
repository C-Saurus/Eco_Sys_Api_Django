from djongo import models


# Create your models here.
class OperatingSystem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    display_size = models.FloatField()
    storage_capacity = models.IntegerField()
    ram_size = models.IntegerField()
    processor = models.CharField(max_length=255)
    operating_system = models.ForeignKey(OperatingSystem, on_delete=models.CASCADE)
    camera_resolution = models.IntegerField()
    battery_capacity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to="img/phones_images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
