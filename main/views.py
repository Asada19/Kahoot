from django.shortcuts import render

# Create your views here.
from drf_yasg.utils import swagger_auto_schema

from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.perimissions import IsOwner
from main.serializers import *
from main.services import *
from user.models import User
from user.serializers import UserSerializer


class QuizAPIView(generics.ListAPIView):
    """
    Список всех тестов
    """
    permission_classes = [IsAuthenticated]
    serializer_class = QuizSerializer
    
    def get_queryset(self):
        queryset = Quiz.objects.filter(group__in=self.request.user.group.all())
        return queryset
    
    def get(
            self,
            request,
            format=None,
            **kwargs):

        queryset = self.get_queryset()
        serializer = self.get_serializer_class(queryset, many=True)
        return Response(serializer.data)


class QuizDetail(generics.RetrieveAPIView):
    """
    Детализация Теста по ID
    """
    serializer_class = QuizSerializer

    def get(self, request, quiz_id):
        """ Вытаскиваем тесты """
        """ ниже фильтрация тестов по группам относящиеся к юзеру """
        queryset = Quiz.objects.filter(id=quiz_id, group__in=request.user.group.all())
        if queryset:
            serializer = QuizSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response('User has not permission')


class GetAnswerAPIView(generics.CreateAPIView):
    """
    Ответ на вопрос
    """
    serializer_class = GetAnswerSerializer
    permission_classes = [IsOwner, ]

    def get_object(self):
        """ Вытаскивает ответы по id полученные из запроса """
        answer_id = self.request.data.get("answer")
        answer = Answer.objects.get(id=answer_id)
        return answer

    def post(self, request, quiz_id, question_id, **kwargs):
        """ POST - запрос который вытаскивает время из запроса, и отправляет ответ """
        queryset = self.get_object()
        answer_time = request.data.get('answer_time')
        user = User.objects.get(pk=request.user.pk)
        print(user.quizz_and_ans)
        if str(question_id) not in request.user.answered_questions:
            # request.user.answered_questions.update({question_id: 0})
            get_score(request, answer_time, question_id, queryset)  # Бизнес логика заключенная в service.py
            count_passed_test(request)
            global_rank(request)
            # local_group_rank(request, **kwargs)
            return Response('Successfully created')
        else:
            return Response('You answered on this question')


