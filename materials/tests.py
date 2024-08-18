from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@sky.com')
        self.course = Course.objects.create(title='Python', description='Django')
        self.lesson = Lesson.objects.create(title='Основы программирования', course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        url = reverse('materials:lessons_create')
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'New Lesson',
            'description': 'Описание нового урока',
            'course': self.course.pk,
            'owner': self.user.pk
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.count(), 2)

    def test_lesson_retrieve(self):
        url = reverse("materials:lessons_retrieve", args=(self.lesson.pk,))
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
