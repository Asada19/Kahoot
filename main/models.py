from django.contrib.auth.models import Group
from django.db import models

from user.models import User


class Quiz(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='quiz')
    is_active = models.BooleanField(default=True, verbose_name='Активно:')

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тест'

    def __str__(self):
        return self.title


class Question(models.Model):
    description = models.TextField(verbose_name='Вопрос')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='question')
    timer = models.PositiveIntegerField(default=20)
    point = models.PositiveIntegerField(default=100)
    image = models.ImageField(blank=True, upload_to='Images')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопрос'

    def __str__(self):
        return self.description


class Answer(models.Model):
    description = models.CharField(max_length=300, verbose_name='Ответ')
    choice = models.BooleanField(default=False, verbose_name='Правильный ответ')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответ'

    def __str__(self):
        return self.description


class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journal')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='journal')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='journal')

    class Meta:
        verbose_name = 'Записи'
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'Journal'


