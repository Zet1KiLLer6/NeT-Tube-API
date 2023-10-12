import os
from celery import Celery
from celery.beat import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_spam': {
        'task': 'account.tasks.send_spam',
        'schedule': crontab(day_of_week='saturday')
    }
}