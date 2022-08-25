from ast import And
from django.contrib import admin
from main.models import *
import nested_admin


class AnswerInline(nested_admin.NestedStackedInline):

    model = Answer
    max_num = 4 
    extra = 4

class QuestionInline(nested_admin.NestedStackedInline):
    inlines = [AnswerInline]
    model = Question
    extra = 4


# class QuestionAdmin(nested_admin.NestedStackedInline):
#     inlines = [AnswerInline, ]

class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline, ]

#
admin.site.register(Quiz, QuizAdmin)
# admin.site.register(Question,)



