from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    stock_quantity = models.IntegerField(
        null=True,
        blank=True,
        help_text="Leave blank to disable stock tracking for this product.",
    )

    @property
    def is_in_stock(self):
        """Returns True if the product is available to purchase."""
        if self.stock_quantity is None:
            return True
        return self.stock_quantity > 0

    @property
    def is_low_stock(self):
        """Returns True if stock is tracked and at or below the low threshold."""
        if self.stock_quantity is None:
            return False
        return 0 < self.stock_quantity <= 5

    @property
    def average_rating(self):
        """Calculate average rating from user reviews."""
        reviews = self.reviews.all()
        if reviews.exists():
            total = sum(r.rating for r in reviews)
            return round(total / reviews.count(), 1)
        return None

    def __str__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(
        choices=RATING_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('product', 'user')

    def __str__(self):
        return f'Review for {self.product.name} by {self.user.username}'
