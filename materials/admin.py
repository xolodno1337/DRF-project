from django.contrib import admin
from materials.models import Course, Lesson
from users.models import User, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('course', 'title')


@admin.register(Payment)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_course', 'payment_lesson', 'payment_sum', 'payment_method')
