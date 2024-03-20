from rest_framework import serializers
from .models import Item, Category


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
