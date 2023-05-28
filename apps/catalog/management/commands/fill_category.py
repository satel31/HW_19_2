from django.core.management import BaseCommand
from apps.catalog.models import Category

class Command(BaseCommand):
    def handle(self, *args, **options):

        category_list = [
            {'category_name': 'Beverages', 'description': 'Soft drinks, coffees, teas, beers, and ales'},
            {'category_name': 'Confections', 'description': 'Desserts, candies, and sweet breads'},
            {'category_name': 'Dairy Products', 'description': 'Cheese, milk, yogurt, quark'},
            {'category_name': 'Grains/Cereals', 'description': 'Breads, crackers, pasta, and cereal'},
            {'category_name': 'Meat/Poultry', 'description': 'Prepared meats'},
            {'category_name': 'Seafood', 'description': 'Seaweed and fish'},
        ]

        Category.objects.all().delete()

        categories_to_create = []

        for category in category_list:
            categories_to_create.append(Category(**category))

        Category.objects.bulk_create(categories_to_create)