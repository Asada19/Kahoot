from .serializers import *


def get_score(request, answer_time, question_id, answer):
    time = Question.objects.get(id=question_id).timer
    point = Question.objects.get(id=question_id).point

    if answer.choice:
        if answer_time < time:
            request.user.score += point - (point / time * answer_time)
            request.user.save()
        print(request.user.score)














