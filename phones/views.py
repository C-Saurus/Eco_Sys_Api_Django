from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Item, OperatingSystem, Brand
from .serializers import ItemSerializer, OperatingSystemSerializer, BrandSerializer


# Create your views here.
@api_view(["GET"])
def getAllPhones(*args, **kwargs):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def getDetail(request, id, *args, **kwargs):
    try:
        item_instance = Item.objects.get(id=id)
    except:
        return Response(
            {"res": "Phones with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    serializer = ItemSerializer(item_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def createItem(request, *args, **kwargs):
    try:
        OperatingSystem.objects.get(id=request.data.get("operating_system"))
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
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WriteApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. Update
    def put(self, request, id, *args, **kwargs):
        try:
            item = Item.objects.get(id=id)
        except:
            return Response(
                {"res": "Object with phone id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = ItemSerializer(instance=item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 2. Delete
    def delete(self, request, id, *args, **kwargs):
        try:
            item = Item.objects.get(id=id)
        except:
            return Response(
                {"res": "Object with phones id does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        item.delete()
        return Response({"res": "Object deleted!"}, status=status.HTTP_200_OK)


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def createOperationSystem(request, *args, **kwargs):
    serializer = OperatingSystemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def getAllopsys(request, *args, **kwargs):
    opsys = OperatingSystem.objects.all()
    serializer = OperatingSystemSerializer(opsys, many=True)
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
