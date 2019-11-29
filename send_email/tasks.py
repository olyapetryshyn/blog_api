from django.core.mail import send_mail
from blog_api.celery import app


@app.task(queue='mailing')
def send_email():
    send_mail(subject='Personal blog.', message='Hello from the crew at Personal blog!',
              from_email='olya.petryshyn@gmail.com', recipient_list=['olha.petryshyn@vakoms.com'])
