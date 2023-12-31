from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .serializers import UserSerializer, UserMenuSerializer, MessageSerializer
from .models import Message
from .models import Room, CustomUser
from .pagination import DefaultPagination


class RegisterUser(mixins.CreateModelMixin, GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserMenu(mixins.RetrieveModelMixin, mixins.CreateModelMixin, GenericAPIView):
    serializer_class = UserMenuSerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        return Room.objects.all

    def get(self, request, *args, **kwargs):
        owner = get_object_or_404(CustomUser, username=self.kwargs['id'])
        queryset = Room.objects.filter(owner=owner)
        serializer = UserMenuSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        # id value is set in self kwargs
        context.update({'user_id': self.kwargs['id']})
        return context

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RoomMessages(ModelViewSet):
    serializer_class = MessageSerializer
    pagination_class = DefaultPagination
    filter_backends = [SearchFilter]
    search_fields = ['content']

    def get_queryset(self):
        room = get_object_or_404(Room, name=self.kwargs['room_pk'])
        queryset = Message.objects.order_by('-timestamp').filter(room=room)
        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'user_id': self.kwargs['id'], 'room_id': self.kwargs['room_pk']})
        return context