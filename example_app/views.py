from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions



def index_view(request):
    return render(request, 'index.html')


class StupidAPIView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, format=None):
        return Response({'message': 'success!'})


