"""example_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from example_app.views import index_view, SecretListAPIView, SecretDetailAPIView, ObtainAuthToken, UserDetailAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/api-token-auth/$', ObtainAuthToken.as_view(), name="obtain_auth_token"),
    url(r'^api/secrets/$', SecretListAPIView.as_view(), name="secret_list_api_view"),
    url(r'^api/secrets/(?P<pk>\d+)/$', SecretDetailAPIView.as_view(), name="secret_detail_api_view"),
    url(r'^api/users/(?P<pk>\d+)/$', UserDetailAPIView.as_view(), name="user_detail_api_view"),
    url(r'^', index_view, name="index_view"),
]
