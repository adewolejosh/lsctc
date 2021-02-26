
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *


User = get_user_model()


class CreateProfileView(APIView):

    def post(self, request):
        email = request.data.get('email')
        username = request.data.get('username')
        serializer = CreateAccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(is_active=False)
        domain = get_current_site(request)

        # mailing logic

        return \
            email.send,\
            Response(
                {
                    'detail': 'account created subject to activation',
                    'user_data': UserSerializer(user).data
                },
                status=status.HTTP_200_OK
            )
