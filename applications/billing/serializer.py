from rest_framework import serializers

from applications.cert.models import User


class ProductCreateListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"