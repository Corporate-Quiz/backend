from django.db import models
from django.contrib.auth import get_user_model
from user.models import Department

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Тег'
    )
    color = models.CharField(
        max_length=7,
        verbose_name='Цвет',
        blank=True
    )

    class Meta():
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class QuizLevel(models.Model):
    name = models.CharField(
        max_length=50, verbose_name='Наименование уровня'
    )
    description = models.CharField(
        max_length=240, verbose_name='Описание уровня'
    )

    class Meta:
        verbose_name = 'Уровень квиза'
        verbose_name_plural = 'уровни квиза'

    def __str__(self):
        return f'{self.name}'


class Quiz(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Наименование квиза'
    )
    description = models.CharField(
        max_length=240,
        verbose_name='Описание квиза'
    )
    image = models.ImageField(
        verbose_name='изображение',
        upload_to='quizes/image/',
        blank=True
    )
    directory = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        related_name='quizes',
        verbose_name='Направление',
        blank=True,
        null=True
    )
    level = models.ForeignKey(
        QuizLevel,
        on_delete=models.SET_NULL,
        related_name='quizes',
        verbose_name='Уровень квиза',
        blank=True,
        null=True
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='quizes',
        verbose_name='Теги',
        blank=True,
    )
    duration = models.SmallIntegerField(
        verbose_name='Время прохождения в минутах'
    )

    @property
    def question_amount(self):
        return self.questions.count()

    class Meta:
        verbose_name = 'Квиз'
        verbose_name_plural = 'Квизы'

    def __str__(self):
        return f'{self.name}'


class Question(models.Model):
    text = models.CharField(
        max_length=240,
        verbose_name='Вопрос'
    )
    image = models.ImageField(
        upload_to='questions/image/',
        verbose_name='изображение',
        blank=True
    )
    quiz = models.ForeignKey(
        Quiz,
        related_name='questions',
        on_delete=models.CASCADE,
        verbose_name='Квизы',
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return f'{self.text}'


class Answer(models.Model):
    text = models.CharField(
        max_length=240,
        verbose_name='Текст ответа'
    )
    image = models.ImageField(
        verbose_name='изображение',
        upload_to='answers/image/',
        blank=True
    )
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers'
    )
    isAnswerRight = models.BooleanField(verbose_name='правельный ответ')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return f'{self.text}'


class Statistic(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='statistic',
        verbose_name='пользователь'
    )
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='statistic',
        verbose_name='Квиз'
    )
    wrong_answers = models.SmallIntegerField(
        verbose_name='Неправильные ответы'
    )

    @property
    def count_questions(self):
        return self.quiz.questions.count()

    class Meta:
        verbose_name = 'Статистика квиза'
        verbose_name_plural = 'Статистика квизов'

    def __str__(self):
        return f'{self.user.email} - {self.quiz.name}'


class AssignedQuiz(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='assigned',
        verbose_name='пользователь'
    )
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name='assigned',
        verbose_name='Квиз'
    )

    class Meta:
        verbose_name = 'Назначенный квиз'
        verbose_name_plural = 'Назначенные квизы'

    def __str__(self):
        return f'{self.user.email} - {self.quiz.name}'