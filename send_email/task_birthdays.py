from django.core.mail import send_mail
from blog_api.celery import birthday_app


@birthday_app.task
def monthly_birthdays():
    send_mail(subject='Monthly birthdays',
              message="Hey! Don't forget about monthly birthday celebration of some of your colleagues.",
              from_email='olya.petryshyn@gmail.com',
              recipient_list=['olha.petryshyn@vakoms.com'])
