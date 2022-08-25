from django.contrib import admin

# Register your models here.
from user.models import User, LeaderBoard


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'login', 'score', 'rank', 'phone_number']
    exclude = ['quizz_and_ans', 'password', 'last_login', 'activation_code']
    list_display_links = ['name', 'login']
    search_fields = ['name', 'second_name', 'phone_number', 'login']
    list_filter = ['group']
    ordering = ['rank']
    readonly_fields = ['passed_tests', 'rank', 'score']


@admin.register(LeaderBoard)
class LeaderAdmin(UserAdmin):
    list_display = ['name', 'login', 'score', 'rank', 'passed_tests']

    def has_add_permission(self, request):
        obj = super().has_add_permission(request)
        if obj:
            obj = False
        return obj


