from django.contrib import admin

from .models import Category, Product, Review


# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "rating",
        "stock_quantity",
        "image",
    )
    list_editable = ("stock_quantity",)
    ordering = ("sku",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "rating", "title", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("product__name", "user__username", "title")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
