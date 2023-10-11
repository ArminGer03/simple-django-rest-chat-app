from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer, UserMenuSerializer


class RegisterUser(mixins.CreateModelMixin, GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserMenu(mixins.RetrieveModelMixin, mixins.CreateModelMixin, GenericAPIView):
    serializer_class = UserMenuSerializer

    def get(self, request, id, **kwargs):
        return Response(id)
        # return self.create(request, *args, **kwargs)

    def post(self, request, id, *args, **kwargs):
        return self.create(request, *args, **kwargs, context={'user_id': id})