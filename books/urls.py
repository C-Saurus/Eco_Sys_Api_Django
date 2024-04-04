from django.urls import path, include
from .views import (
    getAllBook,
    getAllCate,
    getDetail,
    createBook,
    createCate,
    createAuthor,
    getAllAuthor,
    WriteApiView,
)

urlpatterns = [
    path("", getAllBook),
    path("cate/", getAllCate),
    path("author/", getAllAuthor),
    path("<int:id>/", getDetail),
    path("newBook/", createBook),
    path("newCate/", createCate),
    path("newAuthor/", createAuthor),
    path("modify/<int:id>/", WriteApiView.as_view()),
]
