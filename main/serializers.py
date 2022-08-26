from rest_framework import serializers

from main.models import *


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'description', 'choice']


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'description', 'answer']


class QuizSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'group', 'question']


class GetAnswerSerializer(serializers.Serializer):
    answer = serializers.IntegerField(required=True)
    answer_time = serializers.IntegerField(required=True)



# question = Question.objects.all()

# class GroupSerializer(serializers.Serializer):
#     name = Quiz.objects.all(title=question.quiz)
#     count_test = Quiz.objects.all().get(id=question.id)



