import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.models import Item as BookItem
from books.serializers import ItemSerializer as BookSerializer
from clothes.models import Item as ClothesItem
from clothes.serializers import ItemSerializer as ClothesSerializer
from phones.models import Item as PhoneItem
from phones.serializers import ItemSerializer as PhonesSerializer
from rest_framework import status


@api_view(["GET"])
def SearchByKeyWord(request, keyword):
    # Tìm kiếm sản phẩm trong mỗi loại và lọc theo keyword
    books = BookItem.objects.filter(title__icontains=keyword)
    clothes = ClothesItem.objects.filter(name__icontains=keyword)
    phones = PhoneItem.objects.filter(name__icontains=keyword)
    bookInstance = BookSerializer(books, many=True)
    clotheInstance = ClothesSerializer(instance=clothes, many=True)
    phoneInstance = PhonesSerializer(instance=phones, many=True)
    products = []
    products.append({"book": bookInstance.data})
    products.append({"clothes": clotheInstance.data})
    products.append({"phones": phoneInstance.data})
    json_string = json.dumps(products)
    # print(json_string)

    return Response(products, status=status.HTTP_200_OK)


def obj_dict(obj):
    return obj.__dict__
