
from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Profile


User = get_user_model()


class CreateAccountSerializer(serializers.Serializer, metaclass=None):

    class Meta:
        model = Profile
        readonly_fields = []

    def validate_email(self, obj):
        email = obj['email']
        if User.objects.get(email__iexact=email).exists:
            pass

    def validate_username(self, obj):
        username = obj['username']
        if User.objects.get(username__iexact=username).exists:
            pass


class UserSerializer(serializers.Serializer, metaclass=None):
    pass
