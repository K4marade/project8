from django.core.management.base import BaseCommand
from products.models import Product, Category
from django.db import transaction, DatabaseError
from django.conf import settings
import requests
import os
import json


class Database:

    def __init__(self):
        pass

    ########################################################
    #### If you wish to work with locals json files ########
    #### (comment the other same methods further below) ####
    ########################################################

    # if you'd like to refresh your local data :
    # @staticmethod
    # def refresh_data():
    #     categories_data = requests.get(
    #         "https://fr.openfoodfacts.org/categories.json"
    #     )
    #     categories = []
    #     data = categories_data.json()['tags']
    #     for category in data:
    #         categories.append(category['name'])
    #
    #     f = open(os.path.join(settings.BASE_DIR, 'api_data_files/of_api_cat.json'), "w")
    #     f.write(str(categories_data.text))
    #     f.close()
    #
    #     for cat in categories[:30]:
    #         payload = {
    #             "action": "process",
    #             "tagtype_0": "categories",
    #             "tag_contains_0": "contains",
    #             "tag_0": str(cat),
    #             "json": "true"
    #         }
    #         ret_aliments = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", params=payload)
    #         f = open(os.path.join(settings.BASE_DIR, "api_data_files/of_api_ali" + str(cat) + ".json"), "w")
    #         f.write(str(ret_aliments.text))
    #         f.close()
    #
    # @staticmethod
    # def get_categories(quantity):
    #     """Method that gets categories from Open Food Facts' API"""
    #     categories = []
    #     with open(os.path.join(settings.BASE_DIR, "api_data_files/of_api_cat.json"), "r") as file:
    #         file = file.read()
    #
    #     data = json.loads(file)
    #     data = data['tags']
    #     for category in data:
    #         categories.append(category['name'])
    #     return categories[:quantity]
    #
    # @staticmethod
    # def get_aliments(category):
    #     """Method that gets aliments from Open Food Facts' API"""
    #     aliments = dict()
    #     for cat in category:
    #         aliments[cat] = []
    #
    #         with open(os.path.join(
    #                 settings.BASE_DIR,
    #                 "api_data_files/of_api_ali"
    #                 + str(cat) + ".json"
    #         )) as file:
    #             file = file.read()
    #         ret_aliments = json.loads(file)
    #         aliments[cat].append(ret_aliments)
    #     return aliments

    ########################################################
    #### If you wish to work with locals json files ########
    #### (comment the other same methods further below) ####
    ########################################################

    # Live data :
    @staticmethod
    def get_categories(quantity):
        """Method that gets categories from Open Food Facts' API
        and returns them into a list"""

        get_data = requests.get("https://fr.openfoodfacts.org/categories.json")
        if get_data.status_code == 200:
            categories = []
            data = (get_data.json()['tags'])
            for category in data:
                categories.append(category['name'])
            return categories[:quantity]

    @staticmethod
    def get_aliments(category):
        """Method that gets aliments from Open Food Facts' API
        according to categories and returns them into a list"""

        aliments = dict()
        for cat in category:
            aliments[cat] = []
            payload = {
                "action": "process",
                "tagtype_0": "categories",
                "tag_contains_0": "contains",
                "tag_0": str(cat),
                "json": "true"
            }
            ret_aliments = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?", params=payload)
            if ret_aliments.status_code == 200:
                ret_aliments = ret_aliments.json()
                aliments[cat].append(ret_aliments)
        return aliments

    @staticmethod
    def cleaned_data(aliments):
        """Method that takes all data from API's aliments and
        returns a list with only the needed values"""

        lst_data = []

        # make sure each product has the needed information
        for aliment in aliments:
            for products in aliment['products']:
                valid_tag = ["product_name_fr",
                             "nutriscore_grade",
                             "url",
                             "image_url",
                             "image_small_url",
                             "url",
                             "image_nutrition_url"]
                if not all(tag in products for tag in valid_tag):
                    pass
                else:
                    if products['product_name_fr'] != '':  # make sure each product has a name
                        data = [products['code'],
                                products['product_name_fr'],
                                products['nutriscore_grade'],
                                products['image_url'],
                                products['image_small_url'],
                                products['url'],
                                products['image_nutrition_url']]
                        lst_data.append(data)
            return lst_data

    def insert_data(self):
        with transaction.atomic():
            categories = self.get_categories(30)
            aliments = self.get_aliments(categories)

            # keep only needed product information
            for cat, elements in aliments.items():
                aliments[cat] = self.cleaned_data(elements)

            # insert categories in database
            for cat in categories:
                category = Category(name=cat)
                category.save()

            # insert products in database with a many to many relationship with categories
            for cat, elements in aliments.items():
                category = Category.objects.get(name=cat)
                for data in elements:
                    category.products.create(barcode=data[0],
                                             name=data[1],
                                             nutriscore=data[2],
                                             image=data[3],
                                             small_image=data[4],
                                             url=data[5],
                                             nutrition_img=data[6])


class Command(BaseCommand):
    help = "Insert data into pur_beurre database"

    def add_arguments(self, parser):
        parser.add_argument('add_data', type=str)

    def handle(self, *args, **options):
        if options['add_data']:
            try:
                if Product.objects.exists() or Category.objects.exists():
                    pass
                else:
                    db = Database()

                    #######################################
                    ### If you wish to refresh OFF data ###
                    #######################################
                    # self.stdout.write(self.style.WARNING("Refreshing data, please wait..."))
                    # db.refresh_data()
                    # self.stdout.write(self.style.SUCCESS("Data refreshed"))
                    #######################################
                    ### If you wish to refresh OFF data ###
                    #######################################

                    self.stdout.write(self.style.WARNING("Inserting data into DB..."))
                    db.insert_data()
                    self.stdout.write(self.style.SUCCESS("Data inserted successfully !"))

            except DatabaseError:
                self.stderr.write(self.style.ERROR('Failed to insert data.'))
