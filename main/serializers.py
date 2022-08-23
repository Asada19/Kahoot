from rest_framework import serializers

from main.models import *


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'group', 'question']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['question'] = QuestionSerializer(instance.question.all(), many=True, context=self.context).data
        return representation


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['id', 'description', 'answer']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['answer'] = AnswerSerializer(instance.answer.all(), many=True, context=self.context).data
        return representation


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'description', 'choice']


class GetAnswerSerializer(serializers.Serializer):
    answer = serializers.IntegerField(required=True)
    answer_time = serializers.IntegerField(required=True)



# question = Question.objects.all()

# class GroupSerializer(serializers.Serializer):
#     name = Quiz.objects.all(title=question.quiz)
#     count_test = Quiz.objects.all().get(id=question.id)



