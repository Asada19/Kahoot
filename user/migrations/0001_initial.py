# Generated by Django 4.1 on 2022-08-18 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=50)),
                ("second_name", models.CharField(blank=True, max_length=50)),
                (
                    "login",
                    models.EmailField(
                        max_length=254, primary_key=True, serialize=False
                    ),
                ),
                ("phone_number", models.CharField(blank=True, max_length=15)),
                ("is_active", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("activation_code", models.CharField(blank=True, max_length=5)),
                (
                    "group",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="auth.group",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
