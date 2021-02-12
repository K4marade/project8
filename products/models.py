from django.db import models


# Create your models here.


class Product(models.Model):
    barcode = models.BigIntegerField()
    name = models.CharField(max_length=250)
    nutriscore = models.CharField(max_length=1)
    image = models.URLField()
    small_image = models.URLField()
    url = models.URLField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=250)
    products = models.ManyToManyField(Product, db_table='assoc_cat_ali', related_name='categories')

    def __str__(self):
        return self.name


class Favorite(models.Model):
    ali_source = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ali_source')
    ali_sub = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ali_sub')

    class Meta:
        unique_together = ('ali_source', 'ali_sub')

    def __str__(self):
        return "{} {}".format(self.ali_source, self.ali_sub)
