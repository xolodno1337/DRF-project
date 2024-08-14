from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название', help_text='Введите название курса')
    image_course = models.ImageField(upload_to="materials/course", verbose_name="Превью курса",
                                     help_text="Загрузите превью курса", **NULLABLE)
    description = models.TextField(verbose_name='Описание курса', help_text='Введите описание курса')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Владелец',
                              help_text='Укажите владельца курса', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', verbose_name='Курс',
                               help_text='Выберите курс')
    title = models.CharField(max_length=50, verbose_name='Название урока', help_text='Введите название урока')
    description = models.TextField(verbose_name='Описание урока', help_text='Введите описание урока')
    image_course = models.ImageField(upload_to="materials/lesson", verbose_name="Превью урока",
                                     help_text="Загрузите превью урока", **NULLABLE)
    video_url = models.URLField(max_length=300, verbose_name="Видео урока", help_text='Загрузите видео урока',
                                **NULLABLE)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Владелец',
                              help_text='Укажите владельца урока', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
