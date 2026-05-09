from django.urls import path

from . import views

urlpatterns = [
    path("", views.view_wishlist, name="wishlist"),
    path("add/<int:product_id>/", views.add_to_wishlist, name="wishlist_add"),
    path("remove/<int:product_id>/", views.remove_from_wishlist, name="wishlist_remove"),
]
