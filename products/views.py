from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm


# Create your views here.


def all_products(request):
    """A view to show all products, including sorting and search queries"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    # Pagination - 12 products per page
    paginator = Paginator(products, 12)
    page = request.GET.get("page")
    try:
        products_page = paginator.page(page)
    except PageNotAnInteger:
        products_page = paginator.page(1)
    except EmptyPage:
        products_page = paginator.page(paginator.num_pages)

    context = {
        "products": products_page,
        "product_count": paginator.count,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
        "paginator": paginator,
        "page_obj": products_page,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """A view to show individual product details"""
    from wishlist.models import WishlistItem

    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.select_related('user').all()
    review_form = ReviewForm()
    user_review = None
    in_wishlist = False

    if request.user.is_authenticated:
        user_review = reviews.filter(user=request.user).first()
        in_wishlist = WishlistItem.objects.filter(
            user=request.user, product=product
        ).exists()

    context = {
        "product": product,
        "reviews": reviews,
        "review_form": review_form,
        "user_review": user_review,
        "in_wishlist": in_wishlist,
    }

    return render(request, "products/product_detail.html", context)


@login_required
def add_review(request, product_id):
    """Add or update a review for a product"""
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        # Check if user already reviewed this product
        existing = Review.objects.filter(product=product, user=request.user).first()
        form = ReviewForm(request.POST, instance=existing)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            action = "updated" if existing else "submitted"
            messages.success(request, f"Your review has been {action}. Thanks!")
        else:
            messages.error(request, "There was an error with your review. Please check and try again.")
    else:
        messages.error(request, "Invalid request.")

    return redirect(reverse("product_detail", args=[product_id]))


@login_required
def add_product(request):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to add product. Please ensure the form is valid."
            )
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to update product. Please ensure the form is valid."
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product from the store (POST only for safety)"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method != "POST":
        messages.error(request, "Invalid request method.")
        return redirect(reverse("products"))

    product = get_object_or_404(Product, pk=product_id)
    name = product.name
    product.delete()
    messages.success(request, f'"{name}" has been deleted.')
    return redirect(reverse("products"))
