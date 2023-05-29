from django.core.mail import send_mail
from django.shortcuts import render

from rest_framework.views import APIView


class ContactView(APIView):
    def post(self, request):
        email = request.data.get('email')
        msg = request.data.get('msg')
        send_mail(
            "Contact",
            msg,
            email,
            ["django.backend.test.mail@gmail.com"],
            fail_silently=False,
        )
