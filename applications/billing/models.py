from django.db import models

# Create your models here.
from applications.produce.models import Production


class Billing(models.Model):
    NATIONAL_CHOICES = (
        '현금',
        '카드',
        '무통장 입금',
    )
    payment_method = models.CharField(max_length=20, choices=NATIONAL_CHOICES, verbose_name=("결제 수단"))
    product = models.ForeignKey(Production, on_delete=models.CASCADE, verbose_name=("주문 번호"))