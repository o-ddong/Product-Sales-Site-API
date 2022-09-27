from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser, models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name=("회원 번호"))

