# Generated by Django 4.2.2 on 2023-07-28 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0013_useranswerlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='userquestion',
            name='is_right',
            field=models.BooleanField(default=False),
        ),
    ]