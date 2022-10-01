from django.db import models

# Create your models here.
from applications.base.models import BaseModel

""" 유저 관리 테이블 """
class User(BaseModel):
    id = models.BigAutoField(primary_key=True, verbose_name=("회원 번호"))
    email = models.CharField(max_length=255, null=True, verbose_name=("이메일"))
    password = models.CharField(max_length=100, null=True, verbose_name=("비밀 번호"))
    name = models.CharField(max_length=20, null=True, verbose_name=("사용자 이름"))
    mdn = models.CharField(max_length=100, null=True, verbose_name=("전화 번호"))
    grade = models.CharField(max_length=15, null=True, verbose_name=("회원 등급"))
    is_admin = models.BooleanField(verbose_name=("관리자 여부"))




