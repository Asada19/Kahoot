from datetime import timedelta, datetime

import jwt
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin, Group,
)

from Kahhot import settings


class UserManager(BaseUserManager):
    def _create(self, login, password, name, **fields):
        login = self.normalize_email(login)
        user = self.model(login=login, name=name, **fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, login, password, name, **fields):
        fields.setdefault('is_active', True)
        fields.setdefault('is_staff', False)
        return self._create(login, password, name, **fields)

    def create_superuser(self, login, password, name, **fields):
        fields.setdefault('is_active', True)
        fields.setdefault('is_staff', True)
        return self._create(login, password, name, **fields)


class User(AbstractBaseUser):
    name = models.CharField(max_length=50, blank=True)
    second_name = models.CharField(max_length=50, blank=True)
    login = models.EmailField(primary_key=True)
    phone_number = models.CharField(max_length=15, blank=True)
    # passed_tests = models.SmallIntegerField(blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.RESTRICT, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=5, blank=True)
    score = models.PositiveIntegerField(default=0)

    objects = UserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.login

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, obj=None):
        return self.is_staff

    def get_all_permissions(self, obj=None):
        return ''





