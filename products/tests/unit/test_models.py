from mixer.backend.django import mixer
import pytest
from products.models import Product, Category


@pytest.mark.django_db
class TestModels:
    """Class that tests products models"""

    def test_product(self):
        """Tests Product model"""

        product = mixer.blend(Product, name='test product', nutriscore='a')
        assert product.name == 'test product'
        assert Product.objects.filter(name='test product').exists() is True
        assert product.nutriscore == 'a'

    def test_category(self):
        """Tests Category model"""

        category = mixer.blend(Category, name='test category')
        assert category.name == 'test category'
