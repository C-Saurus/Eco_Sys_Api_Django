from django.urls import path
from .views import getAllCart, addToCart, updateCart, removeCart

urlpatterns = [
    path("<int:cart_id>/", getAllCart),
    path("new/", addToCart),
    path("update/<int:cart_id>/", updateCart),
    path("remove/<int:cart_id>/", removeCart),
]
