# Generated by Django 4.2.2 on 2023-07-08 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0003_remove_statistic_wrong_answers_question_explanation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to='quizes.answer', verbose_name='Ответ')),
                ('statistic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answers', to='quizes.statistic', verbose_name='Статистика квиза')),
            ],
            options={
                'verbose_name': 'Ответ пользователя',
                'verbose_name_plural': 'Ответ пользователя',
            },
        ),
        migrations.CreateModel(
            name='LastQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='last_question', to='quizes.question', verbose_name='Вопрос')),
                ('statistic', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='last_question', to='quizes.statistic', verbose_name='Последний отвеченный вопрос')),
            ],
            options={
                'verbose_name': 'Последний вопрос',
                'verbose_name_plural': 'Последние вопросы',
            },
        ),
    ]