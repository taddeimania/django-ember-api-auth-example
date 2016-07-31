
from rest_framework import serializers
from example_app.models import Secret

from django.contrib.auth.models import User


class SecretSerializer(serializers.ModelSerializer):

    class Meta:
        model = Secret


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "id"]
