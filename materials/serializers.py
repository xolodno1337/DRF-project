from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from materials.models import Course, Lesson
from users.models import Payment


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    numbers_lesson = SerializerMethodField()

    def get_numbers_lesson(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = '__all__'


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
