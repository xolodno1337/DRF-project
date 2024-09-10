from celery import shared_task
from django.core.mail import send_mail
from config import settings
from materials.models import Subscription


@shared_task
def sending_updates(course):
    """ Отправляет уведомление при обновлении курса. """
    emails = Subscription.objects.filter(course=course.id).values_list('user__email', flat=True)
    subject = 'Обновление материалов курса!'
    message = f'Вышло обновление материалов курса - {course.name}'
    if emails:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=emails
        )
    print('Сообщение отправлено')
