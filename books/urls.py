from django.urls import path, include
from .views import (
    getAllBook,
    getAllCate,
    getDetail,
    createBook,
    createCate,
    WriteApiView,
)

urlpatterns = [
    path("", getAllBook),
    path("cate/", getAllCate),
    path("<int:id>/", getDetail),
    path("newBook/", createBook),
    path("newCate/", createCate),
    path("modify/<int:id>/", WriteApiView.as_view()),
]
