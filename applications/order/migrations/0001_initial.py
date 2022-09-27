# Generated by Django 4.1.1 on 2022-09-27 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delevery_method', models.CharField(max_length=10, verbose_name='배송 방법')),
                ('price', models.IntegerField(verbose_name='결제 금액')),
                ('postalcode', models.IntegerField(verbose_name='우편 번호')),
                ('billing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.billing', verbose_name='결제 수단')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='회원 번호')),
            ],
        ),
    ]
