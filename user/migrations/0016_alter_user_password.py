# Generated by Django 4.1 on 2022-08-26 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_alter_user_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
