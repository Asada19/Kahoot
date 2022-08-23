from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *


app_name = "user"

urlpatterns = [
    path("", UserAPIView.as_view()),
    path("login", LoginView.as_view(), name='user_login'),
    path("sing_up", RegistrationView.as_view(), name='sing_up')
]
