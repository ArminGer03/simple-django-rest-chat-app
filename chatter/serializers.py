from django.db import transaction
from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from .models import CustomUser, Room
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
    class Meta:
        model = Room
        fields = ['name', 'members']

    def create(self, validated_data):
        user_id = self.context['user_id']
        with transaction.atomic():
            #todo authenticate
            owner = get_object_or_404(CustomUser, username=user_id)
            room = Room(
                name=validated_data['name'],
                owner=owner
            )
            room.save()
            room.members.set(validated_data['members'])
            room.members.add(owner)
            return room