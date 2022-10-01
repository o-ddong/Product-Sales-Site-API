from rest_framework import serializers

from applications.billing.models import Product, Payment, History


class ProductCreateListSerializer(serializers.ModelSerializer):
    """
    상품 생성 및 조회
    """
    class Meta:
        model = Product
        fields = "__all__"

class ProductDetailSerializer(serializers.ModelSerializer):
    """
    상품 상세 조회, 수정, 삭제
    """
    class Meta:
        model = Product
        fields = "__all__"

class PaymentCreateListSerializer(serializers.ModelSerializer):
    """
    결제 생성 및 조회
    """
    class Meta:
        model = Payment
        fields = "__all__"

class PaymentDetailSerializer(serializers.ModelSerializer):
    """
    결제 상세 조회, 수정, 삭제
    """
    class Meta:
        model = Payment
        fields = "__all__"

class HistoryCreateListSerializer(serializers.ModelSerializer):
    """
    주문 내역 생성 및 조회
    """
    class Meta:
        model = History
        fields = "__all__"

class HistoryDetailSerializer(serializers.ModelSerializer):
    """
    주문 내역 상세 조회, 수정, 삭제
    """
    class Meta:
        model = History
        fields = "__all__"