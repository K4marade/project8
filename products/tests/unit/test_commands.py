from products.management.commands.db_init import Database


class TestCommands:
    """Class that tests personalised command"""

    def setup_class(self):
        """Method that sets tests parameters"""

        self.d = Database()

    def test_get_categories(self, monkeypatch):
        """Tests the recovery of categories from Open Food Facts'
        by mocking the result of the API call"""

        categories = ["Category_1", "Category_2"]

        class MockRequestResponse:
            status_code = 200

            @staticmethod
            def json():
                return {
                    "tags": [{"name": category} for category in categories]
                }

        def mockreturn(*args):
            mockreturn.params = {"args": args}
            return MockRequestResponse()

        monkeypatch.setattr("requests.get", mockreturn)

        assert self.d.get_categories(2) == categories
        assert mockreturn.params["args"] == (
            "https://fr.openfoodfacts.org/categories.json",
        )

    def test_get_categories_if_requesterror(self, monkeypatch):
        """Tests the return result if an error occurs
        with the OFF API"""

        class MockRequestResponseWithError:
            status_code = 404

        def mockreturn(*args, **kwargs):
            return MockRequestResponseWithError

        monkeypatch.setattr("requests.get", mockreturn)

        assert self.d.get_categories(2) is None
        assert self.d.get_categories("gateaux") is None

    def test_get_aliments(self, monkeypatch):
        """Tests the recovery of aliments according to one category
        from Open Food Facts' by mocking the result of the API call"""

        category = ["Category_1"]
        aliments = {"Category_1": [{"products": [
            {"product_name_fr": "Ali_1"},
            {"product_name_fr": "Ali_2"}
        ]}]}

        class MockRequestResponse:
            status_code = 200

            @staticmethod
            def json():
                return {"products": [{"product_name_fr": "Ali_1"},
                                     {"product_name_fr": "Ali_2"}]}

        def mockreturn(*args, **kwargs):
            return MockRequestResponse

        monkeypatch.setattr("requests.get", mockreturn)

        assert self.d.get_aliments(category) == aliments

    def test_cleaned_data(self):
        """Tests the result of the returned list
        with only useful product info"""

        lst_data = [["476546754", "Ali_1", "e", "image_url",
                     "sm_img_url", "url", "nutri_url"]]
        aliments = [{"products": [{"code": "476546754",
                                   "product_name_fr": "Ali_1",
                                   "nutriscore_grade": "e",
                                   "image_url": "image_url",
                                   "image_small_url": "sm_img_url",
                                   "url": "url",
                                   "image_nutrition_url": "nutri_url"}]
                     }]

        assert self.d.cleaned_data(aliments) == lst_data

    # @pytest.mark.django_db
    # def test_insert_data(self, monkeypatch):
    #     pass

    # def test_get_categories_with_error(self, monkeypatch):
    #     categories = []
    #     class MockRequestResponseWith404:
    #         status_code = 404

    #         def json(self):
    #             pass

    #     def mockreturn(*args):
    #         mockreturn.params = {"args": args}
    #         return MockRequestResponseWith404

    #     monkeypatch.setattr("requests.get", mockreturn)
    #     assert self.d.get_categories(2) is None
