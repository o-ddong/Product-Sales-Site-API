from django.db import models

# Create your models here.
from applications.base.models import BaseModel


class Production(BaseModel):
    price = models.IntegerField(verbose_name=("가격"))
    name = models.CharField(max_length=20, verbose_name=("상품 이름"))
    origin = models.CharField(max_length=20, verbose_name=("원산지"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=("제조 일자"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=("유통 기한"))
