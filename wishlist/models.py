from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class WishlistItem(models.Model):
    """A saved product in a user's wishlist."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="wishlist",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="wishlisted_by",
    )
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-added_at"]
        unique_together = ("user", "product")

    def __str__(self):
        return f"{self.user.username} — {self.product.name}"
