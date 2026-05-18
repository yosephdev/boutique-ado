from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import connection

from products.models import Product


class Command(BaseCommand):
    help = "Load product fixtures only when the product table is empty."

    def handle(self, *args, **options):
        db_settings = connection.settings_dict
        self.stdout.write(
            f"Seed database target: {db_settings['ENGINE']} / {db_settings['NAME']}"
        )

        product_count = Product.objects.count()

        if product_count:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Skipping product seed: database already has {product_count} products."
                )
            )
            return

        call_command("loaddata", "categories", "products")
        product_count = Product.objects.count()
        self.stdout.write(
            self.style.SUCCESS(f"Seeded product fixtures. Product count: {product_count}")
        )
