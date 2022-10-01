from django.db import models

# Create your models here.
from applications.base.models import BaseModel
from applications.cert.models import User

""" 상품 관리 테이블 """
class Product(BaseModel):
    CATEGORY_CHOICES = [
        (1, '과일'),
        (2, '야채'),
        (3, '주스'),
        (4, '장류'),
    ]

    ORIGIN_CHOICES = [
        (1, '제주도'),
        (2, '경상도'),
        (3, '전라도'),
        (4, '충청도'),
        (5, '강원도'),
        (6, '서울시'),
        (7, '경기도'),
    ]

    id = models.BigAutoField(primary_key=True, verbose_name=("상품 번호"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=("회원 번호"))
    name = models.CharField(max_length=20, verbose_name=("상품 이름"))
    price = models.CharField(max_length=20, verbose_name=("상품 가격"))
    description = models.CharField(max_length=255, verbose_name=("상품 설명"))
    stock = models.IntegerField(verbose_name=("재고"))
    category = models.IntegerField(choices=CATEGORY_CHOICES, verbose_name=("상품 종류"))
    origin = models.IntegerField(choices=ORIGIN_CHOICES, verbose_name=("원산지"))

""" 결제 관리 테이블 """
class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        (1, '택배'),
        (2, '방문 수령'),
        (3, '퀵'),
    ]

    id = models.BigAutoField(primary_key=True, verbose_name=("결제 관리 번호"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=("회원 번호"))
    address = models.CharField(max_length=100, null=False, verbose_name=("배송 주소"))
    requirement = models.CharField(max_length=100, verbose_name=("배송 요청 사항"))
    payment_method = models.IntegerField(choices=PAYMENT_METHOD_CHOICES, verbose_name=("배송 방법"))
    price = models.IntegerField(verbose_name=("총 가격"))

""" 주문 내역 관리 테이블 """
class History(BaseModel):
    id = models.BigAutoField(primary_key=True, verbose_name=("주문 내역 관리 번호"))
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, verbose_name=("결제 관리 번호"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=("회원 번호"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=("상품 관리 번호"))


