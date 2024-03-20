from rest_framework import serializers
from .models import OperatingSystem, Item, Brand


class OperatingSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatingSystem
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
