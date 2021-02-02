from django.db import models


# Create your models here.


class Product(models.Model):
    barcode = models.BigIntegerField()
    name = models.CharField(max_length=250)
    nutriscore = models.CharField(max_length=1)
    image = models.URLField()
    url = models.URLField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=250)
    products = models.ManyToManyField(Product, db_table='assoc_cat_ali', related_name='categories')

    def __str__(self):
        return self.name
