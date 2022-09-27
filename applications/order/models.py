from django.db import models

# Create your models here.
from applications.billing.models import Billing
from applications.billing.cert import User


class Ordering(models.Model):
    delevery_method = models.CharField(max_length=10, verbose_name=("배송 방법"))
    billing = models.ForeignKey(Billing, on_delete=models.CASCADE, verbose_name=("결제 수단"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=("회원 번호"))
    price = models.IntegerField(verbose_name=("결제 금액"))
    postalcode = models.IntegerField(verbose_name=("우편 번호"))
