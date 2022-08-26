# Generated by Django 4.1 on 2022-08-25 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_journal'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='passed_members',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='point',
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='timer',
            field=models.PositiveIntegerField(default=20),
        ),
    ]