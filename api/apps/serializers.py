from rest_framework import serializers

from .models import AppModel


class AppModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppModel
        fields = ["name", "api_key"]
        read_only_fields = ["api_key"]
