"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from applications.billing.views import ProductCreateListMixins, ProductDetailMixins, PaymentCreateListMixins, \
    PaymentDetailMixins

urlpatterns = [
    path('product/', ProductCreateListMixins.as_view()),
    path('product/<int:pk>', ProductDetailMixins.as_view()),
    path('payment/', PaymentCreateListMixins.as_view()),
    path('payment/<int:pk>', PaymentDetailMixins.as_view()),
]
