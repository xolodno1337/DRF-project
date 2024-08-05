# Generated by Django 5.0.6 on 2024-08-03 10:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название курса', max_length=50, verbose_name='Название')),
                ('image_course', models.ImageField(help_text='Загрузите превью курса', upload_to='materials/course', verbose_name='Превью курса')),
                ('description', models.TextField(help_text='Введите описание курса', verbose_name='Описание курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название урока', max_length=50, verbose_name='Название урока')),
                ('description', models.TextField(help_text='Введите описание урока', verbose_name='Описание урока')),
                ('image_course', models.ImageField(help_text='Загрузите превью урока', upload_to='materials/lesson', verbose_name='Превью урока')),
                ('video_url', models.URLField(help_text='Загрузите видео урока', max_length=300, verbose_name='Видео урока')),
                ('course', models.ForeignKey(help_text='Выберите курс', on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='materials.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]
