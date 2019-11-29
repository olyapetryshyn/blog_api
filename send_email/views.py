from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
import json
from .tasks import send_email


class SendEmail(APIView):
    def get(self, request):
        send_email.apply_async()
        return HttpResponse(json.dumps({'msg': 'E-mail has been sent.'}), status=status.HTTP_200_OK)
