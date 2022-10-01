from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics

from applications.base.response import operation_deleted, operation_failure
from applications.cert.models import User
from applications.cert.serializer import UserCreateListSerializer, UserDetailSerializer


class UserCreateListMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request)


class UserDetailMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

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
