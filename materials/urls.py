from django.urls import path
from rest_framework.routers import SimpleRouter
from materials.views import CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView, \
    LessonRetrieveAPIView, LessonDestroyAPIView, CourseListAPIView, PaymentListAPIView, SubscriptionAPIView, \
    SubscriptionListAPIView
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register('', CourseViewSet)

urlpatterns = [
    path('lessons/', LessonListAPIView.as_view(), name='lessons_list'),
    path('lessons/<int:pk>', LessonRetrieveAPIView.as_view(), name='lessons_retrieve'),
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lessons_create'),
    path('lessons/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lessons_delete'),
    path('lessons/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lessons_update'),
    path('course/', CourseListAPIView.as_view(), name='course_list'),
    path('payments/', PaymentListAPIView.as_view(), name='payment_list'),
    path('subscription/create/', SubscriptionAPIView.as_view(), name='subscription_create'),
    path('subscription/', SubscriptionListAPIView.as_view(), name='subscription_list'),
]

urlpatterns += router.urls
