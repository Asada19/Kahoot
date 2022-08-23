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
from main.services import get_score
from user.models import User
from user.serializers import UserSerializer


class QuizAPIView(generics.ListAPIView):
    """
    Список всех тестов
    """
    permission_classes = [IsAuthenticated]
    serializer_class = QuizSerializer

    def get(self, request, format=None):
        queryset = Quiz.objects.filter(group_id=request.user.group)
        serializer = QuizSerializer(queryset, many=True)
        return Response(serializer.data)


class QuizDetail(generics.RetrieveAPIView):
    serializer_class = QuizSerializer

    def get(self, request, quiz_id):
        queryset = Quiz.objects.filter(id=quiz_id, group_id=request.user.group)
        if queryset:
            serializer = QuizSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response('User has not permission')


class GetAnswerAPIView(generics.CreateAPIView):
    serializer_class = GetAnswerSerializer
    permission_classes = [IsOwner, ]

    def get_object(self):
        answer_id = self.request.data.get("answer")
        answer = Answer.objects.get(id=answer_id)
        return answer

    def post(self, request, quiz_id, question_id, **kwargs):
        queryset = self.get_object()
        answer_time = request.data.get('answer_time')
        get_score(request, answer_time, question_id, queryset)
        return Response('Successfully created')
