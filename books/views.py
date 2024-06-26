from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Item, Category, Author
from .serializers import ItemSerializer, CategorySerializer, AuthorSerializer


# Create your views here.
@api_view(["GET"])
def getAllBook(*args, **kwargs):
    books = Item.objects.all()
    serializer = ItemSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def getDetail(request, id, *args, **kwargs):
    try:
        book_instance = Item.objects.get(id=id)
    except:
        return Response(
            {"res": "Book with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    serializer = ItemSerializer(book_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def createBook(request, *args, **kwargs):
    serializer = ItemSerializer(data=request.data)
    try:
        Category.objects.get(id=request.data.get("category"))
    except:
        return Response(
            {"res": "Category with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        Author.objects.get(id=request.data.get("author"))
    except:
        return Response(
            {"res": "Author with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def createAuthor(request, *args, **kwargs):
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WriteApiView(APIView):
    # 1. Update
    def put(self, request, id, *args, **kwargs):
        """
        Updates the todo item with given id if exists
        """
        try:
            book = Item.objects.get(id=id)
        except:
            return Response(
                {"res": "Object with book id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = ItemSerializer(instance=book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 2. Delete
    def delete(self, request, id, *args, **kwargs):
        try:
            book = Item.objects.get(id=id)
        except:
            return Response(
                {"res": "Object with book id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        book.delete()
        return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def createCate(request, *args, **kwargs):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def getAllCate(request, *args, **kwargs):
    cates = Category.objects.all()
    serializer = CategorySerializer(cates, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def getAllAuthor(request, *args, **kwargs):
    cates = Author.objects.all()
    serializer = AuthorSerializer(cates, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
