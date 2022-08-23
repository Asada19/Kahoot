from django.contrib import admin

# Register your models here.
from user.models import User

@admin.register(User)
class UserAdmni(admin.ModelAdmin):
    list_display = ['name',]