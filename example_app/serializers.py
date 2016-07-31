
from rest_framework import serializers
from example_app.models import Secret


class SecretSerializer(serializers.ModelSerializer):

    class Meta:
        model = Secret
