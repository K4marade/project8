from django.db import models
from django.conf import settings


class Product(models.Model):
    """Class that stores OpenFoodFacts aliments, related to
    :model:`products.Category` and :model: `products.Favorite`
    """

    barcode = models.BigIntegerField()
    name = models.CharField(max_length=250)
    nutriscore = models.CharField(max_length=1)
    image = models.URLField()
    small_image = models.URLField()
    url = models.URLField()
    nutrition_img = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Class that stores OpenFoodFats categories,
    related to :model:`products.Product`
    """

    name = models.CharField(max_length=250)
    products = models.ManyToManyField(Product,
                                      db_table='assoc_cat_ali',
                                      related_name='categories')

    def __str__(self):
        return self.name


class Favorite(models.Model):
    """Class that stores user saved substitute, related to
    :model:`products.Product` and :model: account.UserAuth"""

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    ali_source = models.ForeignKey(Product,
                                   on_delete=models.CASCADE,
                                   related_name='ali_source')
    ali_sub = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='ali_sub')

    class Meta:
        unique_together = ('user_id', 'ali_sub')

    def __str__(self):
        return "{} {} {}".format(self.user_id, self.ali_source, self.ali_sub)
