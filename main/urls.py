from django.urls import path

from main.views import *

urlpatterns = [
    path('quiz', QuizAPIView.as_view(), name='list_quiz'),
    path('quiz/<int:quiz_id>/', QuizDetail.as_view(), name='quiz_detail'),
    path('quiz/<int:quiz_id>/<int:question_id>/', GetAnswerAPIView.as_view(), name='post_answer'),
]

