# Generated by Django 4.2.2 on 2023-08-11 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achivement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название достижения')),
                ('description', models.TextField(verbose_name='Описание достижения')),
                ('image', models.ImageField(blank=True, upload_to='achivements/image/', verbose_name='изображение')),
                ('num_of_completed', models.PositiveIntegerField(default=0, verbose_name='Завершенных квизов')),
                ('num_of_passed', models.PositiveIntegerField(default=0, verbose_name='Пройденных квизов')),
                ('num_of_failed', models.PositiveIntegerField(default=0, verbose_name='Проваленных квизов')),
                ('num_of_assigned', models.PositiveIntegerField(default=0, verbose_name='Пройденных назначенных квизов')),
                ('num_of_questions', models.PositiveIntegerField(default=0, verbose_name='Отвечено вопросов')),
                ('num_of_right_questions', models.PositiveIntegerField(default=0, verbose_name='Правильно отвеченных вопросов')),
                ('num_of_wrong_questions', models.PositiveIntegerField(default=0, verbose_name='Неверно отвеченных вопросов')),
                ('time_in_quizes', models.PositiveIntegerField(default=0, verbose_name='Время прохождения пройденных квизов (сек)')),
                ('level', models.PositiveIntegerField(default=0, verbose_name='Уровень пользователя')),
            ],
            options={
                'verbose_name': 'Достижение',
                'verbose_name_plural': 'Достижения',
            },
        ),
        migrations.CreateModel(
            name='UserAchivement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points_to_get', models.PositiveIntegerField(default=0, verbose_name='Очков для получения')),
                ('points_now', models.PositiveIntegerField(default=0, verbose_name='Набранно очков')),
                ('achived', models.BooleanField(default=False, verbose_name='Достижение получено')),
                ('get_date', models.DateField(blank=True, null=True, verbose_name='Дата получения достижения')),
                ('achivement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_achivements', to='ratings.achivement', verbose_name='Достижение')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_achivements', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Достижение пользователя',
                'verbose_name_plural': 'Достижения пользователей',
            },
        ),
        migrations.RemoveField(
            model_name='userachvment',
            name='achivment',
        ),
        migrations.RemoveField(
            model_name='userachvment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Achivment',
        ),
        migrations.DeleteModel(
            name='UserAchvment',
        ),
        migrations.AddField(
            model_name='achivement',
            name='user',
            field=models.ManyToManyField(related_name='achivements', through='ratings.UserAchivement', to=settings.AUTH_USER_MODEL),
        ),
    ]
