from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Item, Category, Brand
from .serializers import ItemSerializer, CategorySerializer, BrandSerializer


# Create your views here.
@api_view(["GET"])
def getAllClothes(*args, **kwargs):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def getDetail(request, id, *args, **kwargs):
    try:
        item_instance = Item.objects.get(id=id)
    except:
        return Response(
            {"res": "Clothes with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    serializer = ItemSerializer(item_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def createItem(request, *args, **kwargs):
    serializer = ItemSerializer(data=request.data)
    try:
        Category.objects.get(id=request.data.get("category"))
    except:
        return Response(
            {"res": "Category with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        Brand.objects.get(id=request.data.get("brand"))
    except:
        return Response(
            {"res": "Brand with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
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
        try:
            item = Item.objects.get(id=id)
        except:
            return Response(
                {"res": "Object with clothes id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = ItemSerializer(instance=item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 2. Delete
    def delete(self, request, id, *args, **kwargs):
        item = Item.objects.get(id=id)
        if not item:
            return Response(
                {"res": "Object with clothes id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        item.delete()
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


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def createBrand(request, *args, **kwargs):
    serializer = BrandSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def getAllBrand(request, *args, **kwargs):
    brands = Brand.objects.all()
    serializer = BrandSerializer(brands, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
