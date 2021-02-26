
from smtplib import SMTPAuthenticationError

from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *


User = get_user_model()


class CreateProfileView(APIView):

    def post(self, request):
        user_email = request.data.get('email')
        user_username = request.data.get('username')
        serializer = CreateAccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        domain = get_current_site(request)
        mail_subject = 'Activate your Budgito account'
        message = render_to_string('account_activation_email.html', {
            'user': user_username,
            'domain': domain,
        })
        to_email = serializer.validated_data.get('email')
        # mailing logic
        email = EmailMessage(subject=mail_subject, body=message, to=[user_email])

        try:
            email.send()
            user = serializer.save(is_active=False)
            Response(
                {
                    'detail': 'account created subject to activation',
                    'user_data': UserSerializer(user).data
                },
                status=status.HTTP_200_OK
            )
        except SMTPAuthenticationError:
            return Response(
                {'detail': 'smtp authentication failed'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
