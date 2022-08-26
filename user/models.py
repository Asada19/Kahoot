from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin, Group, UserManager,)


class MyUserManager(BaseUserManager):
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
    group = models.ManyToManyField(Group, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=5, blank=True)
    score = models.PositiveIntegerField(default=0, blank=True)
    answered_questions = models.JSONField(default=dict, blank=True, null=True)
    quizz_and_ans = models.JSONField(default=dict, blank=True, null=True)
    passed_tests = models.SmallIntegerField(blank=True, null=True)
    rank = models.PositiveIntegerField(default=0, blank=True)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.login

    def list_of_groups(self):
        return ', '.join(map(str, self.group.all()))

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, obj=None):
        return self.is_staff

    def get_all_permissions(self, obj=None):
        return ''

    objects = MyUserManager()


class LeaderBoard(User):

    class Meta:
        verbose_name = "Таблица лидеров"
        verbose_name_plural = verbose_name
        proxy = True

    def __str__(self):
        return 'Leaders'

