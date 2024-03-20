from django.urls import path
from .views import getAllCart, addToCart, updateCart, removeCart, createCate

urlpatterns = [
    path("<int:cart_id>/", getAllCart),
    path("new/", addToCart),
    path("newCate/", createCate),
    path("update/<int:cart_id>/", updateCart),
    path("remove/<int:cart_id>/", removeCart),
]
