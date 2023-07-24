# Generated by Django 4.2.2 on 2023-07-24 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0008_quiz_threshold'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=240, verbose_name='Текст ответа')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers_list', to='quizes.answer', verbose_name='ОТвет из списка')),
            ],
            options={
                'verbose_name': 'Ответ из списка',
                'verbose_name_plural': 'Ответы из списка',
            },
        ),
    ]
