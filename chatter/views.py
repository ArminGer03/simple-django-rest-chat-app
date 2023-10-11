from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, get_object_or_404
from .serializers import UserSerializer, UserMenuSerializer
from .models import Room, CustomUser


class RegisterUser(mixins.CreateModelMixin, GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserMenu(mixins.RetrieveModelMixin, mixins.CreateModelMixin, GenericAPIView):
    serializer_class = UserMenuSerializer

    def get(self, request, id, **kwargs):
        owner = get_object_or_404(CustomUser, username=id)
        queryset = Room.objects.get(owner=owner)
        serializer = UserMenuSerializer(queryset, many=True)
        return Response(serializer.data)
        # return self.create(request, *args, **kwargs)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        # id value is set in self kwargs
        context.update({'user_id': self.kwargs['id']})
        return context

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)