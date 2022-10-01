from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models
from applications.base.models import BaseModel



""" 유저 관리 테이블 """
class User(AbstractBaseUser, BaseModel):
    objects = UserManager()

    id = models.BigAutoField(primary_key=True, verbose_name=("회원 번호"))
    email = models.EmailField(max_length=255, unique=True, null=False, verbose_name=("이메일"))
    password = models.CharField(max_length=100, null=False, verbose_name=("비밀 번호"))
    name = models.CharField(max_length=20, null=True, default=None, verbose_name=("사용자 이름"))
    mdn = models.CharField(max_length=100, null=True, default=None, verbose_name=("전화 번호"))
    grade = models.CharField(max_length=15, null=True, default=None, verbose_name=("회원 등급"))
    is_admin = models.BooleanField(default=False, verbose_name=("관리자 여부"))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']


