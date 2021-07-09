"""arena URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from gamers.views import UserRegistrationAPIView, UsersProfileAPIView, UserSearchAPIView, UserUpdateAPIView

app_name = 'users'

urlpatterns = [
    path('sign-up/', UserRegistrationAPIView.as_view(), name='create'),
    path('me/', UsersProfileAPIView.as_view(), name='login'),
    path('search/', UserSearchAPIView.as_view(), name='get_users'),
    path('update/', UserUpdateAPIView.as_view(), name='update-bio')
]
