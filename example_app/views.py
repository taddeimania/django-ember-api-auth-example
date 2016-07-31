from django.shortcuts import render
from rest_framework.generics import ListAPIView

from example_app.models import Secret
from example_app.serializers import SecretSerializer


def index_view(request):
    return render(request, 'index.html')


class SecretListAPIView(ListAPIView):
    serializer_class = SecretSerializer
    queryset = Secret.objects.all()
