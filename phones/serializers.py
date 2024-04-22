from rest_framework import serializers
from .models import OperatingSystem, Item, Brand


class OperatingSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatingSystem
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["brand"] = BrandSerializer(instance.brand).data
        representation["operating_system"] = OperatingSystemSerializer(
            instance.operating_system
        ).data
        return representation


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
