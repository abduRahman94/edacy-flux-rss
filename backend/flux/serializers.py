from rest_framework import serializers


class FluxSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()

