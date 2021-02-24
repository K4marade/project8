from mixer.backend.django import mixer
import pytest
from products.models import Product, Category


@pytest.mark.django_db
class TestModels:

    def test_product(self):
        product = mixer.blend(Product, name='test product', nutriscore='a')
        assert product.name == 'test product'
        assert Product.objects.filter(name='test product').exists() is True
        assert product.nutriscore == 'a'

    def test_category(self):
        category = mixer.blend(Category, name='test category')
        assert category.name == 'test category'
