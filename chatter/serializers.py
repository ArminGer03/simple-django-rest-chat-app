from django.db import transaction
from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from .models import CustomUser, Room, Message
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(str(e))
        return value

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserMenuSerializer(serializers.ModelSerializer):
    member_usernames = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ['name', 'members', 'member_usernames']

    def get_member_usernames(self, obj):
        return [member.username for member in obj.members.all()]

    def create(self, validated_data):
        user_id = self.context['user_id']
        with transaction.atomic():
            owner = get_object_or_404(CustomUser, username=user_id)
            room = Room(
                name=validated_data['name'],
                owner=owner
            )
            room.save()
            room.members.set(validated_data['members'])
            room.members.add(owner)
            return room


class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ['sender_username', 'content', 'timestamp']
        extra_kwargs = {'sender_username': {'read_only': True}}

    def get_sender_username(self, obj):
        return obj.sender.username

    def create(self, validated_data):
        room_name = self.context['room_id']
        room = get_object_or_404(Room, name=room_name)
        user_id = self.context['user_id']
        sender = get_object_or_404(CustomUser, username=user_id)
        return Message.objects.create(room=room, sender=sender, **validated_data)