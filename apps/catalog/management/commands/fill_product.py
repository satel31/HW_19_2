from django.core.management import BaseCommand
from apps.catalog.models import Product, Category

class Command(BaseCommand):
    def handle(self, *args, **options):
        beverages = Category.objects.get(category_name='Beverages')
        confections = Category.objects.get(category_name='Confections')
        dairy = Category.objects.get(category_name='Dairy Products')
        cereals = Category.objects.get(category_name='Grains/Cereals')
        meat = Category.objects.get(category_name='Meat/Poultry')
        seafood = Category.objects.get(category_name='Seafood')

        product_list = [
            {'product_name': 'Sasquatch Ale', 'description': 'An American Strong Ale style beer',
             'category': beverages, 'unit_price': '14', 'preview': 'products/2020-10-06_00-16-56.png'},
            {'product_name': 'Pavlova', 'description': 'A meringue-based dessert',
             'category': confections, 'unit_price': '17', 'preview': 'products/2020-10-06_00-16-56_dA4sgtP.png'},
            {'product_name': 'Camembert Pierrot', 'description': 'A french cheese',
             'category': dairy, 'unit_price': '34', 'preview': ''},
            {'product_name': 'Filo Mix', 'description': 'Healthy cereal snacks',
             'category': cereals, 'unit_price': '7', 'preview': ''},
            {'product_name': 'Wagyu steak', 'description': 'A Japanese Wagyu steak',
             'category': meat, 'unit_price': '24', 'preview': ''},
            {'product_name': 'Norwegian trout', 'description': 'A fillet of norwegian red fish',
             'category': seafood, 'unit_price': '15', 'preview': 'products/2020-10-06_00-16-56_CTf69Q4.png'},
            {'product_name': 'Swallow', 'description': 'Swallow accelerates the regeneration of Vitality.',
             'category': beverages, 'unit_price': '100', 'preview': 'products/6267110735a41aeae146f552cb06c595.png'},
        ]

        Product.objects.all().delete()

        products_to_create = []

        for product in product_list:
            products_to_create.append(Product(**product))

        Product.objects.bulk_create(products_to_create)