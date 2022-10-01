from rest_framework import serializers

from applications.cert.models import User


class ProductCreateListSerializer(serializers.ModelSerializer):
    """
    상품 생성 및 조회
    """
    class Meta:
        model = User
        fields = "__all__"

class ProductDetailSerializer(serializers.ModelSerializer):
    """
    상품 상세 조회, 수정, 삭제
    """
    class Meta:
        model = User
        fields = "__all__"

class PaymentCreateListSerializer(serializers.ModelSerializer):
    """
    결제 생성 및 조회
    """
    class Meta:
        model = User
        fields = "__all__"

class PaymentDetailSerializer(serializers.ModelSerializer):
    """
    결제 상세 조회, 수정, 삭제
    """
    class Meta:
        model = User
        fields = "__all__"