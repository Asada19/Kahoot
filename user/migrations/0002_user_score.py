# Generated by Django 4.1 on 2022-08-22 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='score',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
