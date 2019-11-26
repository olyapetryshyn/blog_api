from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_email():
    send_mail('Personal blog.', 'This proofs that the task worked!',
              'olya.petryshyn@gmail.com', ['davacic818@exserver.top'])
    return None
