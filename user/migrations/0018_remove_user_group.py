# Generated by Django 4.1 on 2022-08-26 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_alter_user_managers_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='group',
        ),
    ]
