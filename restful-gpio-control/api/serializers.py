from rest_framework import serializers
from .models import ARRCModels

class ARRCSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    data = serializers.CharField(max_length=50)
    user = serializers.CharField(max_length=50)
    date = serializers.DateTimeField(required=False)
    def create(self, validated_data):
        return ARRCModels.objects.create(**validated_data)
