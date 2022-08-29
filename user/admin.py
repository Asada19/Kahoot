from django.contrib import admin

from main.services import global_rank
from user.models import User, LeaderBoard


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['name', 'second_name', 'login', 'password', 'group', 'is_active',
              'is_staff', 'score', 'rank', 'phone_number', 'answered_questions']
    list_display = ['name', 'second_name', 'login', 'list_of_groups', 'score', 'rank', 'phone_number']
    exclude = ['quizz_and_ans', 'last_login', 'activation_code']
    list_display_links = ['name', 'login']
    search_fields = ['name', 'second_name', 'phone_number', 'login']
    list_filter = ['group']
    ordering = ['rank']
    readonly_fields = ['passed_tests', 'rank', 'score']

    # позволяет захешировать пароль юзера созданного в админке
    def save_model(self, request, obj, form, change):
        if not change:
            password = obj.password
            obj.set_password(password)
        super().save_model(request, obj, form, change)


@admin.register(LeaderBoard)
class LeaderAdmin(UserAdmin):
    fields = ['name', 'second_name', 'login', 'password', 'group', 'score', 'rank', 'passed_tests', 'phone_number']
    list_display = ['name', 'second_name', 'login', 'list_of_groups', 'score', 'rank', 'passed_tests', 'phone_number']

    def has_add_permission(self, request):
        obj = super().has_add_permission(request)
        if obj:
            obj = False
        return obj
