from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """serializers a name field for testing APIViews"""
    name = serializers.CharField(max_length=10)
