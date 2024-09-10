from celery import shared_task
from dateutil.relativedelta import relativedelta

from users.models import User
from datetime import timezone


@shared_task
def deactivate_user():
    """Деактивирует пользователя, если он не заходил на сайт в течение 1 месяца."""
    month_ago = timezone.now() - relativedelta(months=1)
    qs = User.objects.filter(is_active=True, last_login__lte=month_ago)
    qs.update(is_acitve=False)
