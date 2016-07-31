from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework import views
from rest_framework import parsers
from rest_framework import renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response

from example_app.models import Secret
from example_app.serializers import SecretSerializer, UserSerializer


def index_view(request):
    return render(request, 'index.html')


class ObtainAuthToken(views.APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.pk})


class SecretListAPIView(ListCreateAPIView):
    serializer_class = SecretSerializer
    queryset = Secret.objects.all()

    def get_queryset(self):
        return Secret.objects.filter(owner=self.request.user)


class SecretDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SecretSerializer
    queryset = Secret.objects.all()

    def get_queryset(self):
        return Secret.objects.filter(owner=self.request.user)


class UserDetailAPIView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.id)
