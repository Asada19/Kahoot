# Generated by Django 4.1 on 2022-08-24 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_answered_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='answered_questions',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]