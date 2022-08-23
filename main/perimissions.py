from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, answer):
        quiz = answer.question.quiz
        user = request.user
        return user.group == quiz.group

