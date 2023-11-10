from rest_framework import serializers
from .models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = [
            "id",
            "address",
            "country",
            "state",
            "city",
            "biography",
            "cpf",
            "user",
        ]
        read_only_fields = ["id", "user"]
