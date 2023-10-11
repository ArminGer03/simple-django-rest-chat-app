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

    def get_serializer_context(self):
        context = super().get_serializer_context()
        # id value is set in self kwargs
        context.update({'user_id': self.kwargs['id']})
        return context

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)