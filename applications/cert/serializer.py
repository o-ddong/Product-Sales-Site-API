from rest_framework import serializers

from applications.cert.models import User


class UserCreateListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['id', 'last_login']

class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"