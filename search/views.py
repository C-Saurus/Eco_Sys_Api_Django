from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.models import Item as BookItem
from clothes.models import Item as ClothesItem
from phones.models import Item as PhoneItem
from rest_framework import status


@api_view(["GET"])
def SearchByKeyWord(request, keyword):
    # Tìm kiếm sản phẩm trong mỗi loại và lọc theo keyword
    books = BookItem.objects.filter(title__icontains=keyword)
    clothes = ClothesItem.objects.filter(name__icontains=keyword)
    phones = PhoneItem.objects.filter(name__icontains=keyword)

    products = []
    products.extend(books)
    products.extend(clothes)
    products.extend(phones)

    return Response(products, status=status.HTTP_200_OK)
