from user.models import User
from .models import Question, Quiz

""" Бизнес логика проекта """


def get_score(
        request,
        answer_time,
        question_id,
        answer):

    current_question = Question.objects.get(id=question_id)
    time = current_question.timer
    point = current_question.point

    if str(question_id) not in request.user.answered_questions:
        request.user.answered_questions.update({str(question_id): 0})
        print(request.user.answered_questions)
        if answer.choice:
            if answer_time < time:
                scores = point - (point / time * answer_time)
                request.user.answered_questions.update({str(question_id): scores})
                request.user.score = sum(request.user.answered_questions.values())
                data_of_test = request.user.quizz_and_ans
                quizzes = Quiz.objects.filter(group__in=request.user.group.all())
                for quiz in quizzes:
                    ides = quiz.id
                    data_of_test.update({ides: [str(i.id) for i in quiz.question.all()]})

    request.user.save()


def global_rank(request):
    user_score = User.objects.all().order_by('-score')
    rank = 1
    for i in user_score:
        i.rank = rank
        i.save()
        print(i, rank)
        rank += 1


def count_passed_test(request):
    quiz_list = request.user.quizz_and_ans
    passed_tests = 0
    for i in quiz_list:
        res = Quiz.objects.filter(id=int(i))
        if set(quiz_list[str(i)]).issubset(set(request.user.answered_questions.keys())):
            passed_tests += 0.5
            print(res)
            for q in res:
                q.passed_members += 0.5

        Quiz.objects.bulk_update(res, fields=['passed_members'])

    request.user.passed_tests = passed_tests
    request.user.save()


