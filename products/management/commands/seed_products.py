from django.core.management import call_command
from django.core.management.base import BaseCommand

from products.models import Product


class Command(BaseCommand):
    help = "Load product fixtures only when the product table is empty."

    def handle(self, *args, **options):
        product_count = Product.objects.count()

        if product_count:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Skipping product seed: database already has {product_count} products."
                )
            )
            return

        call_command("loaddata", "categories", "products")
        self.stdout.write(self.style.SUCCESS("Seeded product fixtures."))
