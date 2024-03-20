from django.urls import path, include
from .views import (
    getAllClothes,
    getAllCate,
    getDetail,
    getAllBrand,
    createBrand,
    createItem,
    createCate,
    WriteApiView,
)

urlpatterns = [
    path("", getAllClothes),
    path("cate/", getAllCate),
    path("brand/", getAllBrand),
    path("<int:id>/", getDetail),
    path("newClothes/", createItem),
    path("newCate/", createCate),
    path("newBrand/", createBrand),
    path("modify/<int:id>/", WriteApiView.as_view()),
]
