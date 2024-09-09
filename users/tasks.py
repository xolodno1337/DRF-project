from celery import shared_task
from users.models import User
from datetime import datetime, timedelta


@shared_task
def deactivate_user():
    users = User.objects.all()
    data_now = datetime.now()
    data_deactivate = timedelta(days=30)
    for user in users:
        if data_now - user.last_login > data_deactivate:
            user.is_active = False
            user.save()
