from ast import And
from django.contrib import admin
from main.models import *
import nested_admin


class AnswerInline(admin.StackedInline):

    model = Answer
    max_num = 4 
    extra = 4


class QuestionInline(admin.StackedInline):
    inlines = [AnswerInline]
    model = Question 
    min_num = 1
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline, ]


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline, ]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)


