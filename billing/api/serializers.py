from rest_framework import serializers
from .models import Items

class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    category = serializers.CharField(max_length=50)
    subcategory = serializers.CharField(max_length=50)
    amount = serializers.IntegerField()