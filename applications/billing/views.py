from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics

from applications.base.response import operation_deleted, operation_failure, certification_failure
from applications.billing.models import Product, Payment, History
from applications.billing.serializer import ProductCreateListSerializer, ProductDetailSerializer, \
    PaymentCreateListSerializer, PaymentDetailSerializer, HistoryCreateListSerializer, HistoryDetailSerializer


class ProductCreateListMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    상품 생성 및 조회
    - 일반 유저 : 조회만 가능
    - 관리자 : 조회, 생성 가능
    """
    queryset = Product.objects.all()
    serializer_class = ProductCreateListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        if not admin_check(data):
            return certification_failure
        return self.create(request)


class ProductDetailMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    """
    특정 상품 조회 및 수정, 삭제
    - 일반 유저 : 상세 조회만 가능
    - 관리자 : 상세 조회, 수정, 삭제 가능
    """
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

    def get(self, request, pk, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        data = request.data.copy()
        if not admin_check(data):
            return certification_failure
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        data = request.data.copy()
        if not admin_check(data):
            return certification_failure
        response = self.destroy(request, *args, **kwargs)
        if response.status_code == 204:
            return operation_deleted
        else:
            return operation_failure

class PaymentCreateListMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    결제 내역 생성 및 조회
    - 일반 유저 : 조회 및 생성 모두 가능
    - 관리자 : 조회 및 생성 모두 가능
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentCreateListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request)


class PaymentDetailMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    """
    결제 내역 상세 조회 및 수정, 삭제
    - 일반 유저 : 상세 조회, 수정, 삭제 모두 가능
    - 관리자 : 상세 조회, 수정, 삭제 모두 가능
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentDetailSerializer

    def get(self, request, pk, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        response = self.destroy(request, *args, **kwargs)
        if response.status_code == 204:
            return operation_deleted
        else:
            return operation_failure

class HistoryCreateListMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    주문 내역 생성 및 조회
    - 일반 유저 : 조회 및 생성 모두 가능
    - 관리자 : 조회 및 생성 모두 가능
    """
    queryset = History.objects.all()
    serializer_class = HistoryCreateListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request)


class HistoryDetailMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    """
    주문 내역 조회 및 수정, 삭제
    - 일반 유저 : 상세 조회, 수정, 삭제 모두 가능
    - 관리자 : 상세 조회, 수정, 삭제 모두 가능
    """
    queryset = History.objects.all()
    serializer_class = HistoryDetailSerializer

    def get(self, request, pk, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        response = self.destroy(request, *args, **kwargs)
        if response.status_code == 204:
            return operation_deleted
        else:
            return operation_failure

def admin_check(data):
    """
    관리자 권한 체크 용도
    """
    if data.get('is_admin') == None:
        return False
    elif data.get('is_admin') == False:
        return False
    else:
        return True