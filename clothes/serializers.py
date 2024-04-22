from rest_framework import serializers
from .models import Category, Item, Brand


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["brand"] = BrandSerializer(instance.brand).data
        representation["category"] = CategorySerializer(instance.category).data
        return representation


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
