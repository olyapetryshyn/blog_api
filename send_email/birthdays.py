from celery import Celery
from celery.schedules import crontab
from django.core.mail import send_mail

birthday_app = Celery('birthdays', broker='redis://127.0.0.1:6379/1')

# disable UTC so that Celery can use local time
birthday_app.conf.enable_utc = False


@birthday_app.task
def monthly_birthdays():
    send_mail(subject='Monthly birthdays',
              message="Hey! Don't forget about monthly birthday celebration of some of your colleagues.",
              from_email='olya.petryshyn@gmail.com',
              recipient_list=['olha.petryshyn@vakoms.com'])


birthday_app.conf.beat_schedule = {
    'see-you-in-ten-seconds-task':
        {
            'task': 'birthdays.monthly_birthdays',
            'schedule': crontab(minute=0, hour=13, day_of_month='24-31', month_of_year='*', day_of_week=5)
        }
}
