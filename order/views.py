from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from user.models import User
from rest_framework import status as statusCode
from .serializers import CartSerializer, CategorySerializer


@api_view(["POST"])
def getAllOrder(request, user_id):
    user = User.objects.get(id=user_id)
    if not user:
        return Response(
            {"res": "User with id does not exists"},
            status=statusCode.HTTP_400_BAD_REQUEST,
        )
    cart_items = Item.objects.filter(user_id=user_id)
    serializer = CartSerializer(cart_items, many=True)
    return Response({"data": serializer.data}, status=statusCode.HTTP_200_OK)


@api_view(["POST"])
def addOrder(request):
    user_id = request.data.get("user_id")
    user = User.objects.get(id=user_id)
    category_id = request.data.get("cate")
    category = Category.objects.get(id=category_id)
    if not user:
        return Response(
            {"res": "User with id does not exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    product_id = request.data.get("product_id")
    quantity = request.data.get("quantity")
    price = request.data.get("price")
    status = request.data.get("status")
    cart_item = Item.objects.create(
        user_id=user,
        cate=category,
        product_id=product_id,
        quantity=quantity,
        price=price,
        status=status,
    )
    return Response({"id": cart_item.id}, status=statusCode.HTTP_201_CREATED)


@api_view(["PUT"])
def updateOrder(request, cart_id):
    cart_item = Item.objects.get(id=cart_id)
    if not cart_item:
        return Response(
            {"res": "Cart with id does not exists"},
            status=statusCode.HTTP_400_BAD_REQUEST,
        )
    quantity = request.data.get("quantity")
    status = request.data.get("status")
    cart_item.quantity = quantity
    cart_item.status = status
    cart_item.save()
    return Response({"id": cart_item.id}, status=statusCode.HTTP_200_OK)


@api_view(["DELETE"])
def cancelOrder(request, cart_id):
    cart_item = Item.objects.get(id=cart_id)
    if not cart_item:
        return Response(
            {"res": "Cart with id does not exists"},
            status=statusCode.HTTP_400_BAD_REQUEST,
        )
    cart_item.delete()
    return Response(
        {"message": "Item has been removed from cart successfully"},
        status=statusCode.HTTP_200_OK,
    )
