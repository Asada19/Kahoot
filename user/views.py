from django.contrib.auth import authenticate, login
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, filters
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from main.services import global_rank
from .serializers import UserSerializer, RegistrationSerializer, LoginSerializer
from .models import User


class UserAPIView(ListAPIView):
    """
    Вывод всех пользователей
    """

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'second_name', 'login']


class RegistrationView(APIView):
    """
    Регистрация
    """
    @swagger_auto_schema(request_body=RegistrationSerializer, tags=['account'])
    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.create()
        global_rank(request)
        return Response('Successfully created', status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    """ Логин """
    serializer_class = LoginSerializer


