# Generated by Django 4.1 on 2022-08-22 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_question_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journal', to='main.answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journal', to='main.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journal', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Записи',
                'verbose_name_plural': 'Записи',
            },
        ),
    ]
