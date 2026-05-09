from django.contrib import admin

from .models import WishlistItem


@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "added_at")
    list_filter = ("added_at",)
    search_fields = ("user__username", "product__name")
    ordering = ("-added_at",)
    readonly_fields = ("added_at",)
