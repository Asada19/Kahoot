from django.contrib import admin
from main.models import *
import nested_admin


class AnswerInline(nested_admin.NestedStackedInline):
    model = Answer
    max_num = 4 
    extra = 4

    def has_delete_permission(self, request, obj=None):
        return False


class QuestionInline(nested_admin.NestedStackedInline):
    inlines = [AnswerInline]
    model = Question
    extra = 1


class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline, ]
    list_display = ['title', 'count_questions', ]


admin.site.register(Quiz, QuizAdmin)




