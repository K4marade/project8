import pytest
import requests
from products.management.commands.db_init import Database


class TestCommands:

    def setup_class(self):
        self.d = Database()

    def test_get_categories(self, monkeypatch):
        categories = ['Category_1', 'Category_2']

        class MockRequestResponse:
            status_code = 200

            @staticmethod
            def json():
                return {
                    'tags': [{'name': category} for category in categories]
                }

        def mockreturn(*args):
            mockreturn.params = {'args': args}
            return MockRequestResponse()

        monkeypatch.setattr('requests.get', mockreturn)

        assert self.d.get_categories(2) == categories
        assert mockreturn.params['args'] == ("https://fr.openfoodfacts.org/categories.json",)

    def test_get_categories_if_requesterror(self, monkeypatch):
        class MockRequestResponseWithError:
            status_code = 404

        def mockreturn(*args, **kwargs):
            return MockRequestResponseWithError

        monkeypatch.setattr('requests.get', mockreturn)

        assert self.d.get_categories(2) is None
        assert self.d.get_categories('gateaux') is None

    # def test_get_aliments(self, monkeypatch):
    #     category = ['Category_1']
    #     aliments = {'Category_1': [{'products': [{'product_name_fr': 'Ali_1'},
    #                                              {'product_name_fr': 'Ali_2'}]}]}
    #
    #     class MockRequestResponse:
    #         status_code = 200
    #
    #         @staticmethod
    #         def json():
    #             aliment = [[i for i in aliments[x]] for x in aliments.keys()]
    #             return {'products': [{'product_name_fr': ali} for ali in aliment]}
    #
    #             # return {
    #             #     'products': [{'product_name_fr': ali} for x, ali in aliment]
    #             # }
    #
    #     def mockreturn(*args, **kwargs):
    #         return MockRequestResponse
    #
    #     monkeypatch.setattr('requests.get', mockreturn)
    #
    #     assert self.d.get_aliments(category) == aliments
    #
    # def test_cleaned_data(self, monkeypatch):
    #     # aliments = ...
    #     pass
    #
    # @pytest.mark.django_db
    # def test_insert_data(self, monkeypatch):
    #     pass

    # def test_get_categories_with_error(self, monkeypatch):
    #     categories = []
    #
    #     class MockRequestResponseWith404:
    #         status_code = 404
    #
    #         def json(self):
    #             pass
    #
    #     def mockreturn(*args):
    #         mockreturn.params = {'args': args}
    #         return MockRequestResponseWith404
    #
    #     monkeypatch.setattr('requests.get', mockreturn)
    #
    #     with pytest.raises(AssertionError):
    #         self.d.get_categories(2)

    # assert self.d.get_categories(2) == categories
