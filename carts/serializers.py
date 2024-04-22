from rest_framework import serializers
from .models import Item, Category


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["cate"] = CategorySerializer(instance.cate).data
        return representation


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
