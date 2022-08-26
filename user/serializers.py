from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User


class LoginSerializer(TokenObtainPairSerializer):
    login = serializers.EmailField()
    password = serializers.CharField(min_length=4)

    def validate_login(self, login):
        if not User.objects.filter(login=login).exists():
            raise serializers.ValidationError('This email does not exists')
        return login

    def validate(self, attrs):
        print(attrs['password'])
        login = attrs.get('login')
        password = attrs.get('password')
        user = User.objects.get(login=login)
        print(user.password)
        if not user.check_password(password):
            raise serializers.ValidationError('Password is not valid')
        return super().validate(attrs)


class UserSerializer(serializers.ModelSerializer):
    """
    Для вывода всех юзеров
    """

    class Meta:
        model = User
        fields = ['name', 'second_name', 'phone_number', 'score', 'passed_tests',
                  'rank', 'list_of_groups']


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    password = serializers.CharField(min_length=4)
    password_confirm = serializers.CharField(min_length=4)

    def validate_email(self, email):
        if User.objects.filter(login=email).exists():
            raise serializers.ValidationError('This email already exists')
        return email

    def validate(self, attrs):
        attrs['login'] = attrs.pop('email')
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('Passwords are not identical')
        return super().validate(attrs)

    def create(self):
        User.objects.create_user(**self.validated_data)

