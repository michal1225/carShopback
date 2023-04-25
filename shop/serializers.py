from rest_framework import serializers

from shop.models import Part


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ['id', 'name', 'description', 'img', 'price']
