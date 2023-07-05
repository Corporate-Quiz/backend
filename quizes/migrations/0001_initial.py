# Generated by Django 4.2.2 on 2023-06-30 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование квиза')),
                ('description', models.CharField(max_length=240, verbose_name='Описание квиза')),
                ('image', models.ImageField(blank=True, upload_to='quizes/image/', verbose_name='изображение')),
                ('duration', models.SmallIntegerField(verbose_name='Время прохождения в минутах')),
                ('directory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quizes', to='user.department', verbose_name='Направление')),
            ],
            options={
                'verbose_name': 'Квиз',
                'verbose_name_plural': 'Квизы',
            },
        ),
        migrations.CreateModel(
            name='QuizLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование уровня')),
                ('description', models.CharField(max_length=240, verbose_name='Описание уровня')),
            ],
            options={
                'verbose_name': 'Уровень квиза',
                'verbose_name_plural': 'уровни квиза',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Тег')),
                ('color', models.CharField(blank=True, max_length=7, verbose_name='Цвет')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wrong_answers', models.SmallIntegerField(verbose_name='Неправильные ответы')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statistic', to='quizes.quiz', verbose_name='Квиз')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statistic', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Статистика квиза',
                'verbose_name_plural': 'Статистика квизов',
            },
        ),
        migrations.AddField(
            model_name='quiz',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quizes', to='quizes.quizlevel', verbose_name='Уровень квиза'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='quizes', to='quizes.tag', verbose_name='Теги'),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=240, verbose_name='Вопрос')),
                ('image', models.ImageField(blank=True, upload_to='questions/image/', verbose_name='изображение')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quizes.quiz', verbose_name='Квизы')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='AssignedQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned', to='quizes.quiz', verbose_name='Квиз')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'Назначенный квиз',
                'verbose_name_plural': 'Назначенные квизы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=240, verbose_name='Текст ответа')),
                ('image', models.ImageField(blank=True, upload_to='answers/image/', verbose_name='изображение')),
                ('is_right', models.BooleanField(verbose_name='правельный ответ')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='quizes.question')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
