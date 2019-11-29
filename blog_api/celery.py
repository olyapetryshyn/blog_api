from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from blog_api import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_api.settings')

celery_scheduled_broker = 'redis://127.0.0.1:6379/1'
birthday_app = Celery('blog_api.send_email', broker=celery_scheduled_broker, backend=celery_scheduled_broker)


celery_broker = "redis://127.0.0.1:6379/0"
app = Celery('blog_api.send_email', broker=celery_broker, backend=celery_broker)

# app.config_from_object('django.conf:settings')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
birthday_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

birthday_app.conf.beat_schedule = {
    'every-last_friday-birthdays':
        {
            'task': 'send_email.task_birthdays.monthly_birthdays',
            'schedule': crontab(minute=10, hour=17, day_of_month='24-31', month_of_year='*', day_of_week='friday')
        }
}


# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))
