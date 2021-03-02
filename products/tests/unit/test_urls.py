from django.urls import reverse, resolve


class TestUrls:
    """Class that tests products url"""

    def test_search_list_url(self):
        """Tests search list url"""

        path = reverse('search')
        assert resolve(path).view_name == 'search'

    def test_results_url(self):
        """Tests results url"""

        path = reverse('results')
        assert resolve(path).view_name == 'results'

    def test_results_url_with_product_id(self):
        """Tests results url with a product id"""

        path = reverse('results', kwargs={'product_id': 1})
        assert resolve(path).view_name == 'results'

    def test_save_url(self):
        """Tests save url"""

        path = reverse('save')
        assert resolve(path).view_name == 'save'

    def test_save_url_with_product_and_substitute_ids(self):
        """Tests save url with a product id and a substitute id"""

        path = reverse('save', kwargs={'product_id': 1, 'substitute_id': 2})
        assert resolve(path).view_name == 'save'

    def test_detail_url(self):
        """Test detail url"""

        path = reverse('detail')
        assert resolve(path).view_name == 'detail'

    def test_detail_url_with_product_id(self):
        """Test detail url with a product id"""

        path = reverse('detail', kwargs={'product_id': 3})
        assert resolve(path).view_name == 'detail'
