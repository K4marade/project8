from django.urls import reverse, resolve


class TestUrls:

    def test_search_list_url(self):
        path = reverse('search')
        assert resolve(path).view_name == 'search'

    def test_results_url(self):
        path = reverse('results')
        assert resolve(path).view_name == 'results'

    def test_results_url_with_product_id(self):
        path = reverse('results', kwargs={'product_id': 1})
        assert resolve(path).view_name == 'results'

    def test_save_url(self):
        path = reverse('save')
        assert resolve(path).view_name == 'save'

    def test_save_url_with_product_and_substitute_ids(self):
        path = reverse('save', kwargs={'product_id': 1, 'substitute_id': 2})
        assert resolve(path).view_name == 'save'

    def test_detail_url(self):
        path = reverse('detail')
        assert resolve(path).view_name == 'detail'

    def test_detail_url_with_product_id(self):
        path = reverse('detail', kwargs={'product_id': 3})
        assert resolve(path).view_name == 'detail'
