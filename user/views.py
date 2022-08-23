from django.contrib.auth import authenticate, login
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, filters
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import *
from .serializers import *


class UserAPIView(ListAPIView):
    """
    Вывод всех пользователей
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'login']

#
# class LoginAPIView(CreateAPIView):
#
#     serializer_class = LoginSerializer
#
#     def post(self, request):
#         data = request.data
#         queryset = User.objects.get(email=data['email'])
#         serializer = LoginSerializer(queryset, data=data)
#         email = request.POST.get('email', )
#         password = request.POST.get('password')
#         user = authenticate(request, email=email, password=password)
#         if serializer.is_valid(raise_exception=True):
#             return Response(status=status.HTTP_200_OK)
#         if user is not None:
#             login(request, user)
#             print(request.user)
#             return Response('Invalid Data')


class RegistrationView(APIView):
    @swagger_auto_schema(request_body=RegistrationSerializer, tags=['account'])
    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)
        print(request.user)
        if serializer.is_valid(raise_exception=True):
            serializer.create()
            return Response('Successfully created', status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


