from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer


class RegisterUser(mixins.CreateModelMixin, GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
