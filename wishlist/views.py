from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import WishlistItem


@login_required
def view_wishlist(request):
    """Display the current user's wishlist."""
    wishlist_items = WishlistItem.objects.filter(
        user=request.user
    ).select_related("product", "product__category")

    context = {
        "wishlist_items": wishlist_items,
    }
    return render(request, "wishlist/wishlist.html", context)


@login_required
def add_to_wishlist(request, product_id):
    """Add a product to the user's wishlist."""
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        _, created = WishlistItem.objects.get_or_create(
            user=request.user, product=product
        )
        if created:
            messages.success(request, f'"{product.name}" added to your wishlist.')
        else:
            messages.info(request, f'"{product.name}" is already in your wishlist.')

    return redirect(reverse("product_detail", args=[product_id]))


@login_required
def remove_from_wishlist(request, product_id):
    """Remove a product from the user's wishlist."""
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        deleted, _ = WishlistItem.objects.filter(
            user=request.user, product=product
        ).delete()
        if deleted:
            messages.success(request, f'"{product.name}" removed from your wishlist.')
        else:
            messages.warning(request, f'"{product.name}" was not in your wishlist.')

    # Redirect back to the page the user came from (wishlist or product detail)
    next_url = request.POST.get("next") or reverse("product_detail", args=[product_id])
    return redirect(next_url)
