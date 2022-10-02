from rest_framework import serializers

from applications.cert.models import User


class UserCreateListSerializer(serializers.ModelSerializer):
    """
    유저 조회 및 생성
    """
    class Meta:
        model = User
        exclude = ['last_login', 'grade','created_at', 'updated_at']

class UserDetailSerializer(serializers.ModelSerializer):
    """
    유저 상세 조회, 수정, 삭제
    """
    class Meta:
        model = User
        fields = "__all__"