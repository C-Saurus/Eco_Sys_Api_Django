from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Item, Category
from .serializers import ItemSerializer, CategorySerializer


# Create your views here.
@api_view(["GET"])
def getAllBook(*args, **kwargs):
    books = Item.objects.all()
    serializer = ItemSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def getDetail(request, id, *args, **kwargs):
    book_instance = Item.objects.get(id=id)
    if not book_instance:
        return Response(
            {"res": "Book with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    serializer = ItemSerializer(book_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def createBook(request, *args, **kwargs):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WriteApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. Update
    def put(self, request, id, *args, **kwargs):
        """
        Updates the todo item with given id if exists
        """
        book = Item.objects.get(id=id)
        if not book:
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
        """
        Deletes the todo item with given id if exists
        """
        book = Item.objects.get(id=id)
        if not book:
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
